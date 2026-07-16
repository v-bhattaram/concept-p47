# ZC-GetBike

## ActionGroup
- **ActionGroupName:** ZC-GetBike
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Beta — Vehicle Crate
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Planet47-Creatures1 Complete
- **ActionGroupStatus:** Active

---
[![Alt text](Bike_Location.jpg)]
[![Alt text](Bike.jpg)]


## ActionItems

### Trigger:SURD Detects Vehicle Crate
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — SURD terminal audio; camera briefly shows a half-buried Zegas vehicle crate under debris
- **BGMusic:** Hopeful beat added to ambient — brief, then returns to normal
- **Dialogs:**
  - SURD: Manifest Bike detected. Designed for rapid traversal across mining terrain.
  - Player: A vehicle crate. Finally, something useful.
  - SURD: It appears when summoned and hides when dismissed. Phase-fold storage, suit-linked recall.
  - Player: It appears when needed and hides when not needed?
  - SURD: Correct. Keep it intact. You are slow without it.
  - Player: Nice to know you are already judging my walking speed.
- **Objectives:**
  - Locate the Zegas vehicle crate in Debris Field Beta
- **GameplayNotes:**
  - player enters Debris Field Beta
  - Side quest ZC-Geography-Cliff-Discovery-1 becomes available after this action group completes.
- Status Draft

---

### Trigger:Clear Debris from Crate
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — physical effort audio when moving debris
- **Dialogs:**
  - Player: This is going to take a few minutes.
  - SURD: You have a pulse cutter.
  - Player: I am not wasting charge on rocks.
  - SURD: Then you have a few minutes.
- **Objectives:**
  - Move or break debris blocking the crate access panel (3 debris pieces)
- **GameplayNotes:**
  - player reaches the crate location
  - Some debris can be pushed. One piece requires a half-charge pulse cutter shot to break.
  - Teaches environmental use of the weapon.
- Status Draft

---

### Trigger:Install Power Cell
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Crate systems boot tone when crystal is inserted
- **Dialogs:**
  - SURD: The bike needs a power cell. Insert a stable energy crystal into the crate port.
  - Player: Same crystals. Every system runs on these.
  - SURD: Efficient design.
  - Player: Or we are dangerously dependent on one resource.
  - SURD: That is also correct.
- **Objectives:**
  - Insert a stable energy crystal into the crate power port (1 crystal)
- **GameplayNotes:**
  - crate access panel exposed
  - Consumes 1 stable crystal from inventory. Player should have sufficient supply from ZC-Energy-Crystals-Intro.
- Status Draft

---

### Trigger:Sync Bike to Suit
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — crate opens, Manifest Bike unfolds and rises into position. Clean, functional, slightly battered.
- **BGMusic:** Vehicle power-on sequence — low mechanical, then steady engine hum
- **Dialogs:**
  - SURD: Syncing bike to suit. Hold still.
  - Player: Synced. What does that mean?
  - SURD: You can summon it from anywhere in open terrain. Dismiss it by pressing and holding. It returns to phase-fold storage.
  - Player: And if I dismiss it near a cliff?
  - SURD: It will be in storage. Not at the bottom of the cliff.
- **Objectives:**
  - Hold still while SURD runs the sync sequence (5 seconds)
- **GameplayNotes:**
  - crate powers up
  - Sync completes automatically. Tutorial overlay explains summon and dismiss controls.
- Status Draft

---

### Trigger:Test Summon and Dismiss
- Trigger Type -> ForcedQuest
- Order 5
- **Cinematic:** No
- **BGMusic:** Engine sound when summoned, fade when dismissed
- **Dialogs:**
  - SURD: Test the summon. Then dismiss it and summon it again.
  - Player: It actually works.
  - SURD: Did you expect otherwise?
  - Player: After today? Yes.
- **Objectives:**
  - Summon the Manifest Bike
  - Ride it briefly to confirm controls
  - Dismiss the bike
  - Summon it again
- **GameplayNotes:**
  - bike synced
  - Bike is now permanently available.
  - Can summon in open terrain. Cannot summon near wreckage, cliffs, or in combat zones.
  - Helps reach distant debris fields, Type-P locations, mineral deposits, and crystal sites.
  - Action group completes after second successful summon.
- Status Draft
