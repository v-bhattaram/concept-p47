# ZC-Energy-Crystals-Intro

## ActionGroup
- **ActionGroupName:** ZC-Energy-Crystals-Intro
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Alpha — Crystal Outcrop
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Minerals-Intro Complete
- **ActionGroupStatus:** Active

---

## ActionItems
[![Alt text](Bike_Location.jpg)]
[![Alt text](Bike.jpg)]
### Trigger:Unusual Energy Detected
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — brief camera drift toward glowing cracks in nearby rock and spilled cargo containers
- **BGMusic:** Low resonant hum added to ambient — crystal energy tone
- **Dialogs:**
  - Player: These crystals are powering the wreckage?
  - SURD: Partially. Zegas catalog lists similar materials as high-density energy storage.
  - Player: Similar materials?
  - SURD: This planet's version is undocumented.
  - Player: Great. Unknown creatures, unknown crystals, no comms.
- **Objectives:**
  - Investigate the glowing energy signatures near the crash site
- **GameplayNotes:**
  - Crystals glow from cracks in rocks and inside broken cargo containers.
  - Some crystals are overloaded and pulse erratically — these must not be touched yet.
- Status Draft

---

### Trigger:Crystal Scanner Unlocked
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — suit HUD updates with crystal scanner overlay
- **BGMusic:** Short electronic unlock tone
- **Dialogs:**
  - SURD: Activating crystal scanner. Stable crystals glow steady. Overloaded crystals pulse. Do not collect a pulsing crystal without stabilizing it first.
  - Player: What happens if I do?
  - SURD: Energy discharge. Painful. Possibly fatal depending on the charge level.
  - Player: Steady glow, safe. Pulsing, do not touch. Understood.
- **Objectives:**
  - Crystal scanner tutorial: activate and scan the outcrop
- **GameplayNotes:**
  - Tutorial introduces stable vs overloaded states, scan-to-identify workflow.
  - Overloaded crystals are a hazard: avoid or stabilize with a mineral component (taught later).
- Status Draft

---

### Trigger:Collect Stable Crystals
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Ambient — crystal hum pulses gently when player is near deposits
- **Dialogs:**
  - Player: These are in almost every crack in the crash zone.
  - SURD: The crash may have fractured subsurface crystal formations. The planet has them in abundance.
  - Player: So we landed on a power source.
  - SURD: Among other things. Collect the stable ones.
- **Objectives:**
  - Scan and collect stable crystal shards (5 units minimum)
  - Avoid overloaded crystals
- **GameplayNotes:**
  - Mix of in-rock deposits and cargo container contents.
  - Player backpack holds up to 3000 units total.
- Status Draft

---

### Trigger:Charge a Zegas System
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Power-up tone when the system activates
- **Dialogs:**
  - SURD: Insert crystals into the damaged comms panel. It needs power before it can even be assessed for repair.
  - Player: Using an undocumented alien crystal to power Zegas corporate hardware.
  - SURD: It is compatible. I confirmed the energy frequency. Mostly.
  - Player: Mostly.
  - SURD: The Zegas team who catalogued similar materials gave it a 94 percent compatibility rating.
  - Player: And the other 6 percent?
  - SURD: I would not recommend testing it today.
- **Objectives:**
  - Use collected crystals to charge the damaged comms panel
- **GameplayNotes:**
  - minimum crystal count reached
  - Unlocks: energy crystal scanner, stable crystal collection, power source for Type-P terminal activation and early weapon systems.
  - Action group completes when the system charges successfully.
- Status Draft
