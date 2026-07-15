# ZC-Opening

## ActionGroup
- **ActionGroupName:** ZC-Opening
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Crash Site — Module Alpha
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On Map Load
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Title Sequence
- Trigger Type -> Cutscene
- Order 1
- **Cinematic:** Yes — black screen, text appears: "4Sagez Presents — 47 Planet"
- **BGMusic:** Silence, then a single low tone builds
- **Dialogs:** None
- **Objectives:** None
- **GameplayNotes:**
  - Text fades. Audio starts with the sound of atmosphere entry — hull friction, wind shear, alarms.
- Status Draft

---

### Trigger:Armada Crash
- Trigger Type -> Cutscene
- Order 2
- **Cinematic:** Yes — camera above Planet 47 atmosphere. Zegas armada ships tear through cloud cover. Multiple hulls break apart across a massive forested region. Fire, debris, falling trees, dust clouds. Ships crash across a wide radius.
- **BGMusic:** Heavy impact audio, distant alarms, fading engine noise
- **Dialogs:** None
- **Objectives:** None
- **GameplayNotes:**
  - Camera settles into one broken Zegas module interior.
  - A cracked emergency kiosk flickers in the smoke. Screen text:
    - ZEGAS CORPORATION ARMADA 47
    - FLIGHT PATH ERROR
    - IMPACT EVENT CONFIRMED
    - SURVIVOR STATUS UNKNOWN
- Status Draft

---

### Trigger:SURD SOS
- Trigger Type -> Cutscene
- Order 3
- **Cinematic:** Yes — kiosk screen, SURD audio over static
- **BGMusic:** Fading alarms, low hum, static bursts
- **Dialogs:**
  - SURD: Critical S.O.S. This is SURD. Orbital Command, can you read me?
  - (Static. No reply.)
  - SURD: Critical S.O.S. This is SURD. Orbital Command, respond.
  - (Static weakens.)
  - SURD: Critical S.O.S. This is SURD. Armada down. Any station, respond.
  - (Static fades.)
  - SURD: Critical S.O.S. Zegas Armada 47. Does anyone copy.
  - (Silence.)
  - SURD: ...S.O.S.
- **Objectives:** None
- **GameplayNotes:**
  - Repeat SOS 5 times. Each transmission is quieter than the last. Final one trails off.
  - Camera drifts from the kiosk through the wrecked module toward a sealed survivor pod.
- Status Draft

---
### Map Over view
![alt text](zc-opening/level1.bmp "Title")
![alt text](zc-opening/level1.bmp "Title")

### Trigger:Wake Up
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — player POV inside cracked pod, blurred vision clears
- **BGMusic:** Low ambient drone, distant fire, wind
- **Dialogs:**
  - Player: (coughs, no words yet)
- **Objectives:**
  - Break open the damaged survivor pod
  - Exit the crashed Zegas module
- **GameplayNotes:**
  - Player forces the pod door open from inside. First player-controlled action.
  - Crawls out into the debris field.
  - Tutorial: movement controls introduced here.
- Status Draft

---
![alt text](zc-opening/level1.bmp "Title")

### Trigger:First Look
- Trigger Type -> ForcedQuest
- Order 5
- **Cinematic:** No
- **BGMusic:** Ambient — wind, fire crackle, distant structural groaning, alien insect sounds
- **Dialogs:**
  - Player: Where is everyone?
  - Player: This was an armada. There should be signals, bodies, something.
  - Player: I need comms. If anyone survived, they will try to reach Orbital Command.
- **Objectives:**
  - Look around the crash zone
  - Find any sign of other survivors
- **GameplayNotes:**
  - No crew members are visible. No bodies are found anywhere.
  - End on player standing alone among the debris, facing open terrain.
  - Action group completes when player walks beyond the module perimeter.
- Status Draft
