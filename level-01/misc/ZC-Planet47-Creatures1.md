# ZC-Planet47-Creatures1

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures1
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Wreckage Path — Type-P Route
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Weapons-Unlock Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Path Blocked
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — camera briefly shows a pack predator in the narrow corridor between two wreck hulls
- **BGMusic:** Low threat tone — not full alert, but the route is clearly not safe
- **Dialogs:**
  - Player: Smaller one. Still not friendly.
  - SURD: Scan complete. Fast predator. Low armor. High bite risk.
  - Player: Your summaries need fewer bite details.
  - SURD: Avoid the mouth.
- **Objectives:**
  - Approach the creature zone
  - Scan the creature from cover
- **GameplayNotes:**
  - player moves toward Type-P route
  - Creature is a pack predator — faster than the large carnivore from the intro but less armored.
  - Player must decide: stealth bypass or stun shot.
  - Side quest ZC-Creature-Discover-2 becomes available after this action group completes.
- Status Draft

---

### Trigger:Choose Approach
- Trigger Type -> ForcedPuzzle
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient continues — tension sustained
- **Dialogs:**
  - SURD: Two options. Crouch through the side passage, or stun it and walk through the center.
  - Player: Which do you recommend?
  - SURD: Stun costs cooldown time and crystal charge. Stealth costs nothing if it works.
  - Player: If it works.
  - SURD: Correct qualifier.
- **Objectives:**
  - Clear the path using stealth bypass or stun shot
- **GameplayNotes:**
  - creature spotted and scanned
  - Both approaches are valid. No wrong answer.
  - Stealth: crouch, move along side passage, no detection.
  - Stun: fire half-charge, creature staggers, walk through center path.
  - If creature detects player without a stun shot, it attacks. Player can still fight it off — this is a learnable loss.
- Status Draft

---

### Trigger:Advance to New Section
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Brief relief tone — urgency settles
- **Dialogs:**
  - Player: New section of the crash field. These containers have Zegas markings I have not seen before.
  - SURD: Secondary cargo drop zone. Type-P search points are in this area.
- **Objectives:**
  - Reach the new debris section beyond the creature zone
- **GameplayNotes:**
  - player reaches the far side of the blocked path
  - Unlocks access to Debris Field Beta, where the Manifest Bike crate is located.
  - Action group completes when player crosses the debris zone perimeter into the new section.
- Status Draft
