# ZC-Operational-Chain-Instructions

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:Orbital Command Reconnects
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No — relay pings from suit, SURD confirms residual signal
- **BGMusic:** Ambient — quiet moment after escape, then comms tone
- **Dialogs:**
  - SURD: The transmission log is intact. Orbital Command is re-pinging using the log frequency.
  - Player: They can reach us?
  - SURD: Briefly. Short burst only. Answer fast.
- **Objectives:**
  - Accept incoming burst signal from Orbital Command
- **GameplayNotes:**
  - player reaches safe zone
  - Uses residual relay connection from Signal Peak — short, one-way burst.
- Status Draft

---

### Trigger:Operational Chain Briefing
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — voice only from suit comms
- **BGMusic:** Static-laced Orbital Command audio over ambient
- **Dialogs:**
  - Orbital Command: Signal holding. Good. Listen carefully. You cannot hold a stable comms link without active Zegas infrastructure.
  - Player: What infrastructure? The armada is gone.
  - SURD: Not all of it. Orbital Command is detecting a Zegas Energy Tower in this sector. Still standing.
  - Orbital Command: Activate the tower. Route power to MATREX. Load MIRA. Get LIRA online. In that order.
  - Player: And then what?
  - Orbital Command: Then we can route an extraction path.
  - SURD: Four systems. One sequence. I will mark the map.
  - Player: Four systems on an alien planet full of carnivores. Good briefing.
  - SURD: You have a bike.
- **Objectives:**
  - Receive and confirm the operational chain directive
- **GameplayNotes:**
  - Chain order is permanent: Energy Tower → MATREX → MIRA → LIRA-X9.
  - Cannot activate systems out of order — each powers the next.
- Status Draft

---

### Trigger:Map Updated
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No — map opens automatically, four markers placed
- **BGMusic:** Map activation tone — four location pings
- **Dialogs:**
  - SURD: Energy Tower marked. Sector East. MATREX, Sector Central. MIRA, Sector Central-West. LIRA-X9, Sector North.
  - Player: They are spread across the entire map.
  - SURD: Mining sites are not built for convenience. They are built for coverage.
  - Player: Great.
- **Objectives:**
  - Review the four operational chain markers on the map
- **GameplayNotes:**
  - All four markers are now visible on the map.
  - Touch Points for the operational chain are now active.
  - Action group completes when player acknowledges the map.
- Status Draft

---

### Trigger:SURD Confirms Sequence
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Ambient — quiet determination tone
- **Dialogs:**
  - SURD: Energy Tower first. Without power, MATREX cannot extract, MIRA cannot process, and LIRA cannot transmit.
  - Player: And LIRA is the exit.
  - SURD: LIRA is the communication chain. The exit marker appears when LIRA locks on Orbital Command.
  - Player: Understood. Let's move.
- **Objectives:**
  - Ride to Energy Tower — Sector East
- **GameplayNotes:**
  - Player is now directed to the Energy Tower.
  - All four markers remain visible on the map for the rest of the level.
- Status Draft
