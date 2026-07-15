# ZC-Orbital-Command-Instrcutions1

## ActionGroup
- **ActionGroupName:** ZC-Orbital-Command-Instrcutions1
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** LIRA-X9 Tower — Sector North
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Operational-Chain-LIRA-Instructions Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Orbital Command Confirms Signal
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No — LIRA tower speaker activates, clean signal for the first time
- **BGMusic:** Clear comms tone — no static for the first time in Level 1
- **Dialogs:**
  - Orbital Command: Survivor confirmed. LIRA operational. MIRA data received. Status report is stronger than expected.
  - Player: We had a lot of obstacles.
  - Orbital Command: We are reading your signal clearly. Full connection holding.
- **Objectives:**
  - Receive Orbital Command confirmation of LIRA status
- **GameplayNotes:**
  - LIRA-X9 online
  - First completely clean comms connection of the level. Signal quality contrast is intentional.
- Status Draft

---

### Trigger:Extraction Route Brief
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient with Orbital Command signal overlay
- **Dialogs:**
  - Orbital Command: We are routing an extraction path from your current position. You need to move northeast. Transit zone. Exit coordinates sent to your suit.
  - Player: What is at the transit zone?
  - Orbital Command: Another crash site from the armada. Possibly habitable modules. Could be supplies, could be personnel.
  - Player: Survivors?
  - Orbital Command: Unknown. Move to the transit zone. Do not linger.
- **Objectives:**
  - Receive transit zone coordinates
  - Acknowledge extraction directive
- **GameplayNotes:**
  - Transit zone = map exit. Player now has a clear direction.
  - "Could be personnel" is deliberately ambiguous — where are the other crew members?
- Status Draft

---

### Trigger:Unidentified Signatures Warning
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Brief tension note — not a jump, just a weight to the words
- **Dialogs:**
  - Orbital Command: One more thing. The MIRA anomaly you flagged — prior extraction activity. That data matches other signals we have been tracking.
  - Player: Then you know who was here before us.
  - Orbital Command: Do not investigate it on Level 1. Move to the transit zone first.
  - SURD: They know what it is.
  - Player: They are not saying.
  - SURD: I noticed.
  - Orbital Command: One final thing. You are not alone on that planet. Take it seriously.
  - Player: We already figured that out.
  - Orbital Command: Not the creatures.
- **Objectives:**
  - Process Orbital Command warning
- **GameplayNotes:**
  - "Not the creatures" is the hook for Syntara Prime — the other presence on the planet.
  - This is the last story beat before the level exit. Do not explain further.
  - Action group completes when comms close.
- Status Draft

---

### Trigger:Move to Exit
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Forward ambient — steady, purposeful, slight undercurrent of unease from the warning
- **Dialogs:**
  - Player: Northeast. Transit zone.
  - SURD: Bike route is clear. I am marking the path.
  - Player: Let's finish this.
- **Objectives:**
  - Ride to the Transit Zone — Sector Northeast (map exit marker)
- **GameplayNotes:**
  - comms close
  - Map exit marker is visible on HUD and map.
  - Straightforward ride to exit — no additional threats on this route.
- Status Draft
