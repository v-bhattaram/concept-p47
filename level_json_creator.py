"""
Scans a level's dialogs/ folder tree and builds the level's game data JSON,
using the same LocationGroup / Location / Trigger headers as the level's
design-doc .md files (e.g. level-01/ZC-GetBike/ZC-Energy-Crystals-Intro.md):

    dialogs/<LocationGroup folder>/<N - Trigger>/<NN>-<character>.mp3
    dialogs/<LocationGroup folder>/<Location folder>/<N - Trigger>/<NN>-<character>.mp3

A LocationGroup folder either holds numbered trigger folders directly
(it IS a single Location), or holds several Location folders that each
hold numbered trigger folders. Both shapes are detected automatically
from the folder tree, no hardcoded names.

Output shape (one file per level):

{
  "level": "level-01",
  "location_groups": [
    {
      "location_group": "ZC-Contact-With-Orbital-Command",
      "locations": [
        {
          "location": "ZC-Contact-With-Orbital-Command",
          "triggers": [
            {
              "Order-Trigger": "1 - Build Comms Relay",
              "trigger": "Build Comms Relay",
              "location$$trigger": "ZC-Contact-With-Orbital-Command$$Build Comms Relay",
              "dialogues": [
                {
                  "character": "SURD",
                  "dialogue": "",
                  "audio_file_location": "dialogs/ZC-Contact-With-Orbital-Command/1 - Build Comms Relay/01-surd.mp3"
                },
                {
                  "character": "Player",
                  "dialogue": "",
                  "audio_file_location_male": "dialogs/.../02-Player-Male.mp3",
                  "audio_file_location_female": "dialogs/.../02-Player-Female.mp3"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

"dialogue" text is pulled from the matching design-doc .md file's
"- **Dialogs:**" script for that trigger (e.g. a flat LocationGroup's
Location "ZC-Contact-With-Orbital-Command" reads from
misc/ZC-Contact-With-Orbital-Command.md; a nested Location like
"ZC-Energy-Crystals-Intro" under LocationGroup "ZC-GetBike" reads from
ZC-GetBike/ZC-Energy-Crystals-Intro.md). Lines are matched to audio files
per-character in order (all SURD lines in order, all Player lines in
order, etc.) since audio file numbering and the script's line order can
drift apart. If a trigger's line count for a character doesn't match its
audio take count for that character, those lines are left blank and a
warning is printed instead of guessing a possibly-wrong pairing.

Re-running this script also preserves any dialogue text already entered
directly in the output JSON (matched by audio file path, and taking
priority over the .md script text) and drops dialogue entries that still
have no text, so the output only ever contains dialogue lines that have
actually been written.
"""

import json
import re
from pathlib import Path

LEVEL_NAME = "level-01"
LEVEL_DIR = Path(__file__).parent / LEVEL_NAME
DIALOGS_DIR = LEVEL_DIR / "dialogs"
OUTPUT_FILE = LEVEL_DIR / "game_data_level01.json"

TRIGGER_FOLDER_RE = re.compile(r"^(\d+)\s*-\s*(.+)$")
FILENAME_RE = re.compile(r"^(\d+)-(.+)$")

CHARACTER_NAMES = ["SURD", "Player", "Orbital Command"]
TRIGGER_BLOCK_RE = re.compile(r"^### Trigger:(.+?)\s*\n(.*?)(?=\n### Trigger:|\Z)", re.DOTALL | re.MULTILINE)
DIALOGS_SECTION_RE = re.compile(r"\*\*Dialogs:\*\*[ \t]*\n((?:[ \t]*-.*(?:\n|$))*)")
DIALOG_LINE_RE = re.compile(r"^\s*-\s*(SURD|Player|Orbital Command)\s*:\s*(.+)$", re.IGNORECASE)


def is_trigger_dir(path: Path) -> bool:
    return path.is_dir() and TRIGGER_FOLDER_RE.match(path.name) is not None


def character_from_token(token: str) -> tuple[str, str | None]:
    """Map a raw filename character token to (display_name, gender)."""
    lower = token.lower()
    if lower.startswith("player"):
        gender = "Male" if "male" in lower and "female" not in lower else (
            "Female" if "female" in lower else None
        )
        return "Player", gender
    if lower == "surd":
        return "SURD", None
    if lower == "orbital-command":
        return "Orbital Command", None
    return token.replace("-", " ").title(), None


def parse_md_dialog_script(md_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Map trigger title -> ordered [(character, line text), ...] from a .md design doc."""
    if not md_path.exists():
        return {}

    text = md_path.read_text(encoding="utf-8")
    script_by_trigger: dict[str, list[tuple[str, str]]] = {}

    for block_match in TRIGGER_BLOCK_RE.finditer(text):
        title = block_match.group(1).strip()
        body = block_match.group(2)

        lines: list[tuple[str, str]] = []
        dialogs_match = DIALOGS_SECTION_RE.search(body)
        if dialogs_match:
            for raw_line in dialogs_match.group(1).splitlines():
                line_match = DIALOG_LINE_RE.match(raw_line)
                if not line_match:
                    continue  # stage direction / parenthetical, no speaker
                raw_character, line_text = line_match.groups()
                character = next(c for c in CHARACTER_NAMES if c.lower() == raw_character.lower())
                lines.append((character, line_text.strip()))

        script_by_trigger[title] = lines

    return script_by_trigger


def md_path_for_location(location_dir: Path, group_dir: Path) -> Path:
    if location_dir == group_dir:
        return LEVEL_DIR / "misc" / f"{location_dir.name}.md"
    return LEVEL_DIR / group_dir.name / f"{location_dir.name}.md"


def load_existing_dialogue_text(path: Path) -> dict[str, str]:
    """Map audio_file_location* -> previously entered dialogue text."""
    if not path.exists():
        return {}

    text_by_audio_path: dict[str, str] = {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

    for location_group in data.get("location_groups", []):
        for location in location_group.get("locations", []):
            for trigger in location.get("triggers", []):
                for dlg in trigger.get("dialogues", []):
                    text = dlg.get("dialogue", "").strip()
                    if not text:
                        continue
                    for key, value in dlg.items():
                        if key.startswith("audio_file_location"):
                            text_by_audio_path[value] = text

    return text_by_audio_path


def build_dialogues(
    trigger_dir: Path,
    trigger_title: str,
    existing_text: dict[str, str],
    md_script: dict[str, list[tuple[str, str]]],
    mismatch_warnings: list[str],
) -> list[dict]:
    mp3_files = sorted(trigger_dir.glob("*.mp3"))

    # group by (number, base_character) so male/female takes of the same
    # line collapse into a single dialogue entry
    groups: dict[tuple[str, str], dict] = {}
    order: list[tuple[str, str]] = []

    for mp3 in mp3_files:
        match = FILENAME_RE.match(mp3.stem)
        if not match:
            continue
        number, raw_token = match.groups()
        base_character, gender = character_from_token(raw_token)
        key = (number, base_character)
        rel_path = (Path("dialogs") / mp3.relative_to(DIALOGS_DIR)).as_posix()

        if key not in groups:
            groups[key] = {"character": base_character, "dialogue": ""}
            order.append(key)

        if base_character == "Player":
            field = f"audio_file_location_{gender.lower()}" if gender else "audio_file_location"
            groups[key][field] = rel_path
        else:
            groups[key]["audio_file_location"] = rel_path

    # fill in text already hand-entered in a previous run
    for key in order:
        entry = groups[key]
        for field, value in entry.items():
            if field.startswith("audio_file_location") and value in existing_text:
                entry["dialogue"] = existing_text[value]
                break

    # fill in remaining blanks from the .md script, matched per-character
    keys_by_character: dict[str, list[tuple[str, str]]] = {}
    for key in order:
        keys_by_character.setdefault(groups[key]["character"], []).append(key)

    lines_by_character: dict[str, list[str]] = {}
    for character, line_text in md_script.get(trigger_title, []):
        lines_by_character.setdefault(character, []).append(line_text)

    for character, keys in keys_by_character.items():
        script_lines = lines_by_character.get(character, [])
        if len(script_lines) != len(keys):
            mismatch_warnings.append(
                f"{trigger_dir.parent.name}/{trigger_dir.name}: {character} has "
                f"{len(keys)} audio take(s) but {len(script_lines)} script line(s) — left blank"
            )
            continue
        for key, line_text in zip(keys, script_lines):
            if not groups[key]["dialogue"].strip():
                groups[key]["dialogue"] = line_text

    return [groups[key] for key in order if groups[key]["dialogue"].strip()]


def build_location(
    location_dir: Path,
    group_dir: Path,
    existing_text: dict[str, str],
    mismatch_warnings: list[str],
) -> dict:
    trigger_dirs = sorted(
        (d for d in location_dir.iterdir() if is_trigger_dir(d)),
        key=lambda d: int(TRIGGER_FOLDER_RE.match(d.name).group(1)),
    )
    md_script = parse_md_dialog_script(md_path_for_location(location_dir, group_dir))

    triggers = []
    for trigger_dir in trigger_dirs:
        title = TRIGGER_FOLDER_RE.match(trigger_dir.name).group(2)
        triggers.append({
            "Order-Trigger": trigger_dir.name,
            "trigger": title,
            "location$$trigger": f"{location_dir.name}$${title}",
            "dialogues": build_dialogues(trigger_dir, title, existing_text, md_script, mismatch_warnings),
        })

    return {"location": location_dir.name, "triggers": triggers}


def build_location_group(group_dir: Path, existing_text: dict[str, str], mismatch_warnings: list[str]) -> dict:
    children = sorted(d for d in group_dir.iterdir() if d.is_dir())

    if children and all(is_trigger_dir(c) for c in children):
        # group_dir IS a single Location
        locations = [build_location(group_dir, group_dir, existing_text, mismatch_warnings)]
    else:
        locations = [build_location(c, group_dir, existing_text, mismatch_warnings) for c in children]

    return {"location_group": group_dir.name, "locations": locations}


def main():
    existing_text = load_existing_dialogue_text(OUTPUT_FILE)
    mismatch_warnings: list[str] = []
    location_group_dirs = sorted(d for d in DIALOGS_DIR.iterdir() if d.is_dir())
    data = {
        "level": LEVEL_NAME,
        "location_groups": [
            build_location_group(d, existing_text, mismatch_warnings) for d in location_group_dirs
        ],
    }

    OUTPUT_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")

    if mismatch_warnings:
        print(f"\n{len(mismatch_warnings)} character/line count mismatch(es) left blank:")
        for warning in mismatch_warnings:
            print(f"  - {warning}")


if __name__ == "__main__":
    main()
