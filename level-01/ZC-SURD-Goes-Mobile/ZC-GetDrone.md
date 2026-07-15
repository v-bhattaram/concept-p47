# ZC-GetDrone

## ActionGroup
- **ActionGroupName:** ZC-GetDrone
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Buried Command Module
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-GetBike Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Find the Type-P Terminal
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Ambient — bike engine sound as player rides between marked locations
- **Dialogs:**
  - SURD: Three possible Type-P locations are marked. Search them in order. The bike will cut the travel time significantly.
  - Player: Finally.
  - SURD: First location: the partially buried command module, northeast sector.
- **Objectives:**
  - Ride the Manifest Bike to the first Type-P location (northeast sector)
  - Search 2 additional marked locations if needed
- **GameplayNotes:**
  - Player uses bike for the first real traversal across open terrain.
  - First Type-P location is the correct one — discovery is not randomized. The other locations are optional to visit but none are active.
  - Side quest ZC-Geography-Water-Discovery-2 becomes available after this action group completes.
- Status Draft

---

### Trigger:Extract the SURD Node
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** Partial — Type-P terminal screen activates as player approaches. Green light. SURD acknowledges the connection.
- **BGMusic:** Clean electronic connection tone
- **Dialogs:**
  - SURD: Type-P connection established. Transfer possible.
  - Player: So you are in this node now?
  - SURD: Correct. I am portable but immobile.
  - Player: That sounds inconvenient.
  - SURD: Find a compatible drone body.
  - Player: Of course you need a body.
  - SURD: A small recon drone will be sufficient. Scout, communicate, shoot, and guide.
  - Player: That is more than sufficient.
- **Objectives:**
  - Activate the Type-P terminal
  - Extract the SURD Node when prompted
- **GameplayNotes:**
  - player reaches buried command module
  - SURD node is now in the player's suit inventory. SURD is portable but silent until inside the drone.
- Status Draft

---

### Trigger:Locate and Repair the Recon Drone
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Ambient — wreckage search atmosphere
- **Dialogs:**
  - SURD: (from suit node, muffled) Compatible drone chassis is approximately forty meters southeast. Zegas recon model. Damaged but repairable.
  - Player: Can you tell anything from in there?
  - SURD: I can interface with suit sensors. Barely. Find the drone faster.
- **Objectives:**
  - Locate the compatible recon drone chassis (40 m southeast)
  - Repair the drone chassis using minerals, energy crystals, and salvage alloy
- **GameplayNotes:**
  - Repair requires: 2 conduit minerals, 2 stable crystals, 1 alloy fragment — all types already known.
  - Drone is recognizable — Zegas corporate markings, compact recon form.
- Status Draft

---

### Trigger:Boot SURD's Portable Body
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Yes — player inserts SURD node into drone chassis. Drone powers on, hovers unsteadily, then stabilizes beside the player. Camera holds on the drone as it rises to eye level.
- **BGMusic:** Boot sequence tone, then the drone hum settles into a steady presence sound
- **Dialogs:**
  - SURD: Portable systems online.
  - Player: You can fly?
  - SURD: Limited altitude. Limited weapon power. Expanded attitude.
  - Player: I regret giving you a body already.
  - SURD: Regret logged. Continuing mission support.
- **Objectives:**
  - Insert the SURD Node into the repaired drone
  - Confirm drone boot sequence completes
- **GameplayNotes:**
  - drone repaired
  - SURD is now a permanent companion drone.
  - Drone capabilities: scout ahead, mark resources, shoot small threats, relay objectives, improve communication range.
  - SURD no longer requires return trips to fixed terminals.
  - Milestone: SURD Portable achieved.
- Status Draft
