# ZC-Food-Water-2

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:Water Cache Located
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Ambient — slight tension, the zone is closer to creature movement
- **Dialogs:**
  - SURD: Water cartridge cache ahead. Three sealed units. One container shows a cracked seal.
  - Player: Compromised how?
  - SURD: Cracked seal on impact. Possible interior contamination. Scan will confirm.
  - Player: I will scan it.
  - SURD: Also: a predator is in the same corridor.
  - Player: Of course it is.
- **Objectives:**
  - Locate the water cache in Container Zone Beta
- **GameplayNotes:**
  - side quest marker activates
  - Cache is positioned inside a creature patrol zone.
  - Player must time the creature's movement to approach safely — reinforces stealth skills.
- Status Draft

---

### Trigger:Wait for Creature to Pass
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Stealth ambient — creature proximity pulse
- **Dialogs:**
  - SURD: Creature is on a short patrol loop. The corridor is clear for about twenty seconds on each pass.
  - Player: Twenty seconds is enough.
  - SURD: If you are fast.
- **Objectives:**
  - Wait for creature to move away from the container corridor
  - Enter and exit the corridor within the patrol gap
- **GameplayNotes:**
  - player in sight of the corridor
  - Simple timed stealth window. If caught: flee zone, wait, retry.
  - No combat required — this is a resource quest, not a combat quest.
- Status Draft

---

### Trigger:Scan and Collect Water Cartridges
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Tense ambient — creature can return if player takes too long
- **Dialogs:**
  - Player: (scanning) First two are clean. Third one — cracked seal confirmed.
  - SURD: Contamination detected inside the third. Do not open it.
  - Player: Leaving it. Taking the two.
  - SURD: Correct call. A contaminated water supply is worse than no supply.
- **Objectives:**
  - Scan all 3 containers in the corridor
  - Collect the 2 clean water cartridges
  - Leave the contaminated container
- **GameplayNotes:**
  - player in corridor with creature away
  - Teaches that not everything is worth taking. Contaminated container is a decision point.
  - If player opens the contaminated container, suit hydration is penalized temporarily.
- Status Draft

---

### Trigger:Exit Before Creature Returns
- Trigger Type -> SideQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Relief tone when player exits the zone
- **Dialogs:**
  - Player: Two out of three. Better than nothing.
  - SURD: Water reserves extended. Hydration is stable for now.
  - Player: Let's not make a habit of this corridor.
  - SURD: Agreed.
- **Objectives:**
  - Exit the creature corridor before patrol returns
- **GameplayNotes:**
  - Side quest complete. Updates player's water reserve status.
- Status Draft
