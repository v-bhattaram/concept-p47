# ZC-Planet47

## ActionGroup
- **ActionGroupName:** ZC-Planet47
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Crash Site — Module Alpha Exterior
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Opening Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Find Comms
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Tense ambient — wind, debris settling, distant fires
- **Dialogs:**
  - Player: None of my comms are working. I need to find another unit.
  - Player: Let me check the crashed pods.
  - Player: If Orbital Command is listening, I need a transmitter strong enough to punch through this atmosphere.
- **Objectives:**
  - Search the debris for a working comms device
  - Inspect 3 broken comms panels in the crash zone
  - Collect usable signal parts from wreckage
- **GameplayNotes:**
  - Place comms parts in 3 or 4 locations within 100 m of Module Alpha.
  - Each part is damaged or missing a power cell. No working device is found yet.
  - Tutorial: scanning and item interaction introduced here.
- Status Draft

---

### Trigger:Suit Up
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient continues — slight tension rise when suit systems activate
- **Dialogs:**
  - Player: The suit is damaged. I need to find the rest of it before the environment kills me.
- **Objectives:**
  - Search the debris for suit components
  - Equip the damaged Zegas survival suit
  - Unlock suit storage and basic HUD functions
  - Scan nearby corporate containers
- **GameplayNotes:**
  - Suit pieces are scattered in debris near Module Alpha.
  - Intro to suit storage system — limited capacity at first.
  - Scanning tutorial: player scans containers to confirm safe contents.
  - Suit expands when player recovers additional Zegas modules later.
- Status Draft

---

### Trigger:Scale of the Crash
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** Partial — camera pulls back from player to show wide terrain as player reaches the ridge
- **BGMusic:** Ambient swells briefly — alien wind, distant bird-like calls, scale implied by silence
- **Dialogs:**
  - Player: The wreckage goes beyond the ridge.
  - Player: This is too much ground to cover on foot.
  - Player: Food, water, comms, survivors. One thing at a time.
- **Objectives:**
  - Reach the ridge overlook at the crash perimeter
- **GameplayNotes:**
  - Player sees: massive terrain, distant cliffs, strange tree lines, distant armada wreckage far beyond walking range.
  - This visual establishes the need for the Manifest Bike later.
  - Action group completes when player reaches the overlook marker.
- Status Draft
