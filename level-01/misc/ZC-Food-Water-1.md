# ZC-Food-Water-1

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:SURD Pings Container Cluster
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No — quest marker activates on map
- **BGMusic:** Ambient — no change
- **Dialogs:**
  - SURD: Food reserves flagged. Three containers within range. Marking them.
  - Player: One at a time. Scan first.
  - SURD: Correct. Unknown compound contamination is possible if a container seal ruptured on impact.
  - Player: I will scan everything.
  - SURD: Survival preference logged.
- **Objectives:**
  - Find 3 Zegas food containers in Container Zone Alpha
- **GameplayNotes:**
  - side quest marker appears
  - Containers are on foot distance — no bike needed.
  - Introduces the scan-before-open discipline.
- Status Draft

---

### Trigger:Scan and Collect
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — alert if scan reveals contamination
- **Dialogs:**
  - Player: (scanning) Clean. Good.
  - (on second container) This one took impact damage. Checking seal.
  - SURD: Seal is intact. Safe to open.
  - Player: And the third?
  - SURD: Third is partially buried. Pull it clear before scanning.
- **Objectives:**
  - Scan all 3 containers
  - Open and collect contents from clean containers
- **GameplayNotes:**
  - player reaches first container
  - All 3 containers in this quest are safe — the contaminated container lesson comes in ZC-Food-Water-2.
  - One container is partially buried (minor interaction: tug it free first).
- Status Draft

---

### Trigger:Ration Pack Inventory Updated
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No — HUD nutrition indicator updates
- **BGMusic:** Short positive tone — survival resource secured
- **Dialogs:**
  - SURD: Ration reserve extended. You have approximately two standard operational days of nutrition at current exertion levels.
  - Player: Two days.
  - SURD: There is more wreckage. More containers.
  - Player: Then we keep looking.
- **Objectives:**
  - Confirm ration pack inventory update on HUD
- **GameplayNotes:**
  - all containers collected
  - Side quest complete. Updates player's food reserve status.
  - Marks these containers as "depleted" — they do not refill.
- Status Draft
