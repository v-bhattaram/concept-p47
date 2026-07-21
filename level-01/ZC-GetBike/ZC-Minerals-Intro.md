# ZC-Minerals-Intro

## ActionGroup
- **ActionGroupName:** ZC-Minerals-Intro
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Alpha — Impact Craters
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Food-Water-Intro Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Tools Need Repair
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Ambient — no change
- **Dialogs:**
  - SURD: Your equipment cannot be repaired with ration packs.
  - Player: I guessed that part.
  - SURD: Search for ferrite mesh, conduit ore, and Zegas alloy fragments.
  - Player: Mining company crashes on a planet and I still have to mine. That tracks.
- **Objectives:**
  - Listen to SURD's repair requirements
- **GameplayNotes:**
  - Brief setup beat. SURD explains what materials are needed and why.
- Status Draft

---

### Trigger:Mineral Scanner Unlocked
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — suit HUD updates with mineral scanner overlay
- **BGMusic:** Short electronic unlock tone
- **Dialogs:**
  - SURD: Activating suit mineral scanner. Use it to identify deposits and salvage grades.
  - Player: How accurate is it?
  - SURD: Sufficient for surface and near-surface deposits. Deeper veins require full mining equipment.
  - Player: Which we do not have.
  - SURD: Correct. Work with what crashed.
- **Objectives:**
  - Scanner tutorial: activate and use the mineral scanner
- **GameplayNotes:**
  - Tutorial introduces scanner overlay, deposit color-coding, and grade ratings.
  - Basic salvage grade shown first — higher grades are rare at this stage.
- Status Draft

---

### Trigger:Find Repair Minerals
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Ambient — light urgency when scanning active deposits
- **Dialogs:**
  - Player: Some of these crash craters exposed rock layers below the surface.
  - SURD: Crash impact does the work that mining equipment normally handles. Collect from the exposed faces.
- **Objectives:**
  - Scan mineral signatures in the crash crater zone
  - Salvage minerals from broken Zegas mining containers (3 containers)
  - Collect exposed surface minerals near the craters (2 deposits)
- **GameplayNotes:**
  - Mix of container salvage and natural deposit collection.
  - Deposits were exposed by crash impact — no drill required.
  - Introduce mineral types: ferrite mesh, conduit ore, alloy fragments.
- Status Draft

---

### Trigger:Return Materials to Fabricator
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** No change
- **Dialogs:**
  - SURD: That is enough to start repairs. The suit fabricator can process these.
  - Player: Where is the fabricator?
  - SURD: Nearby. I am marking it. It is damaged but functional.
- **Objectives:**
  - Deliver collected minerals to the suit fabricator
- **GameplayNotes:**
  - required mineral count reached
  - Unlocks: suit mineral scanner permanently, basic salvage from Zegas mining crates, repair materials for tools and later weapon crafting.
  - Action group completes when materials are delivered to the fabricator.
- Status Draft
