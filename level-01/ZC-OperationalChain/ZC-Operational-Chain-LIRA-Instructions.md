# ZC-Operational-Chain-LIRA-Instructions

## ActionGroup
- **ActionGroupName:** ZC-Operational-Chain-LIRA-Instructions
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** LIRA-X9 Tower — Sector North
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Planet47-Creatures6 Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Reach LIRA-X9 Tower
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Post-combat ambient — quiet intensity, player's breathing, creature gone
- **Dialogs:**
  - Player: LIRA-X9. The last one.
  - SURD: Let me interface. The MIRA data needs to upload before the relay can lock on Orbital Command.
- **Objectives:**
  - Approach the LIRA-X9 tower base
- **GameplayNotes:**
  - Apex predator has retreated. Area is quiet.
  - LIRA-X9 is tall — similar build to Energy Tower but with a large dish array at the top.
- Status Draft

---

### Trigger:SURD Interfaces with LIRA
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** Partial — SURD drone flies up to a drone interface port on the LIRA tower mid-section and connects
- **BGMusic:** Connection tone — clean, establishing
- **Dialogs:**
  - SURD: Interface port located. Connecting now.
  - Player: How long for the upload?
  - SURD: Two minutes at this data volume.
  - Player: Keep watching the perimeter.
  - SURD: I will notify you if anything approaches. Upload in progress.
- **Objectives:**
  - Allow SURD to connect to the LIRA interface port (automated, drone docks)
- **GameplayNotes:**
  - player at tower base
  - Player has a 2-minute wait while SURD uploads. Can patrol the perimeter or use the time for side tasks.
  - Nothing attacks during this wait — it is a deliberate breathing moment after the apex encounter.
- Status Draft

---

### Trigger:Upload MIRA Data
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No — upload progress visible on HUD
- **BGMusic:** Upload progress tone — steady, rising as percentage climbs
- **Dialogs:**
  - SURD: Upload in progress. Seventy percent. Eighty.
  - Player: (quiet) First time I have stood still in hours.
  - SURD: Ninety.
  - Player: Come on.
  - SURD: One hundred. Upload complete.
- **Objectives:**
  - Wait for MIRA data upload to complete (2 minutes real-time)
- **GameplayNotes:**
  - SURD connected
  - Progress displayed on HUD. Player can look around but should stay near the tower.
- Status Draft

---

### Trigger:Activate LIRA-X9
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Yes — LIRA-X9 tower activates with a full sequence. Dish arrays at the top rotate and lock on a bearing. A strong signal pulse shoots upward. The sky briefly lights with a visible transmission beam.
- **BGMusic:** Grand activation sequence — the most significant power-up sound in Level 1
- **Dialogs:**
  - SURD: LIRA-X9 online. Long-range relay is active.
  - SURD: Map exit marker placed. Orbital Command is receiving our full signal.
  - Player: This is the strongest signal we have had since the crash.
  - SURD: And the first one with real data behind it.
- **Objectives:**
  - Confirm LIRA-X9 is online
  - Confirm map exit marker has appeared
- **GameplayNotes:**
  - upload finishes
  - LIRA-X9 online = Touch Point achieved.
  - Milestone: Operational Chain Complete achieved.
  - Map exit marker activates in the Transit Zone — Sector Northeast.
  - Action group completes when player acknowledges both confirmations.
- Status Draft
