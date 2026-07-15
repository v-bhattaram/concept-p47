# ZC-Food-Water-3

## ActionGroup
- **ActionGroupName:** ZC-Food-Water-3
- **ActionType:** SideQuest
- **Level:** Level-01
- **Location:** Wreckage Grid — Hidden Storage Module
- **MarkerVisibility:** On ZC-Food-Water-2 Complete
- **PreReqTrigger:** On ZC-Food-Water-2 Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:SURD Detects High-Value Cache Signal
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No — distinct beacon ping on HUD, different tone from regular containers
- **BGMusic:** Ambient — slight curiosity tone from the unusual signal
- **Dialogs:**
  - SURD: Priority cache signal detected. Zegas corporate priority grade.
  - Player: What does that mean?
  - SURD: It means it was sealed for executives and senior geologists. The supply quality is significantly higher than field ration grade.
  - Player: Finally something with upside.
  - SURD: The lock needs a power cell. Use a spare crystal.
  - Player: Worth it.
- **Objectives:**
  - Follow the priority cache signal to the hidden storage module
- **GameplayNotes:**
  - SURD picks up a strong storage beacon signal
  - Signal comes from a module buried under a debris pile in the Wreckage Grid zone.
  - Requires bike to reach the zone efficiently.
- Status Draft

---

### Trigger:Clear Debris to Access Module
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — physical effort sounds
- **Dialogs:**
  - Player: This one went deep.
  - SURD: Impact buried it. Good news is nothing else found it either.
  - Player: Small victories.
- **Objectives:**
  - Remove or break debris covering the storage module hatch (3 pieces)
- **GameplayNotes:**
  - player reaches the module
  - Mix of push and pulse-cutter debris. One piece is too large to push — requires half-charge shot.
- Status Draft

---

### Trigger:Bypass Lock with Energy Crystal
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No — lock powers on when crystal is inserted, door opens with pressurized release
- **BGMusic:** Lock power-on tone, then pressurized seal opening sound
- **Dialogs:**
  - SURD: Priority lock confirmed. Insert a crystal to power the bypass circuit.
  - Player: (inserts crystal, lock opens)
  - SURD: Zegas executive survival protocol. These caches were stocked for long-duration field operations.
  - Player: How long could someone survive on this?
  - SURD: One person, light exertion: twelve to fifteen days.
- **Objectives:**
  - Insert a stable energy crystal into the lock bypass port (1 crystal)
  - Open the module hatch
- **GameplayNotes:**
  - hatch exposed
  - Consumes 1 crystal. Worth it for the reward.
- Status Draft

---

### Trigger:Secure the Cache
- Trigger Type -> SideQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Short positive tone — a genuine win
- **Dialogs:**
  - Player: High-grade ration packs, sealed water, medical gel. All intact.
  - SURD: Full cache secured. This extends your operational window considerably.
  - Player: Good. Fewer chances to die between meals.
  - SURD: I would phrase that as improved survival margin, but your version is also accurate.
- **Objectives:**
  - Collect all contents: high-grade ration packs, sealed water cartridges, emergency medical gel
- **GameplayNotes:**
  - module open
  - Best food and water yield in Level 1.
  - Medical gel is a new item: heals suit damage / player health. First time this item appears.
  - Side quest complete. Significant reserve update on HUD.
- Status Draft
