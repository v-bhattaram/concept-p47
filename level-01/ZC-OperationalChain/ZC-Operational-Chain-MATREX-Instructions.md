# ZC-Operational-Chain-MATREX-Instructions

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:Ride to MATREX
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Open terrain ride ambient — forward momentum, post-combat calm
- **Dialogs:**
  - SURD: MATREX station is online thanks to the tower. Power feed confirmed.
  - Player: What does MATREX do exactly?
  - SURD: Material Extractor. Processes raw minerals, generates a certified site extraction report, and forwards the data to MIRA.
  - Player: A machine that does paperwork.
  - SURD: A machine that tells Orbital Command the planet has extractable resources worth a rescue operation.
  - Player: I stand corrected. Where is it?
- **Objectives:**
  - Ride to MATREX Station — Sector Central
- **GameplayNotes:**
  - MATREX is visible from distance once in Sector Central — large industrial machine with Zegas markings.
- Status Draft

---

### Trigger:Clear MATREX Input Port
- Trigger Type -> ForcedPuzzle
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — industrial site atmosphere
- **Dialogs:**
  - SURD: Input port is blocked with crash debris. Clear it before depositing.
  - Player: How much?
  - SURD: The port needs to be accessible. Two large pieces and some loose material.
- **Objectives:**
  - Remove debris blocking the MATREX input port (2 large pieces, use pulse cutter)
  - Clear loose material from the port opening
- **GameplayNotes:**
  - player reaches MATREX
  - One debris piece requires pulse cutter to break. One can be pushed clear manually.
  - Reinforces environmental weapon use.
- Status Draft

---

### Trigger:Deposit Minerals
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No — MATREX machine sounds activate when deposit begins
- **BGMusic:** MATREX processing audio — mechanical grinding, conveyor, extraction sounds
- **Dialogs:**
  - SURD: Deposit minerals at the input port. One thousand units minimum.
  - Player: All of them?
  - SURD: The extractor needs enough material to generate a valid site report.
  - Player: That is a lot to carry around a planet full of teeth.
  - SURD: You have been carrying it. Now put it somewhere useful.
- **Objectives:**
  - Deposit a minimum of 1000 mineral units into the MATREX input port
- **GameplayNotes:**
  - input port clear
  - Player must have 1000+ mineral units collected across the level to complete this.
  - If player has fewer than 1000, the MATREX UI shows the shortfall. Player must return to mining before proceeding.
  - Depositing more than 1000 units increases the report quality (no gameplay benefit in Level 1, but flagged for future levels).
- Status Draft

---

### Trigger:Extraction Complete
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — MATREX finishes processing, a data packet indicator lights up on the machine face, then transmits to the MIRA marker on the map
- **BGMusic:** Processing completion tone — clean, mechanical satisfaction
- **Dialogs:**
  - SURD: Extraction complete. Data packet sent to MIRA.
  - Player: MIRA is next.
  - SURD: Correct. And the data will already be waiting when we arrive.
  - Player: Efficient.
  - SURD: MATREX was designed to be efficient. The planet was not.
- **Objectives:**
  - Confirm MATREX data packet sent to MIRA
- **GameplayNotes:**
  - Trigger condition: Minimum deposit threshold reached
  - MATREX deposit = Touch Point achieved.
  - MIRA marker activates with a pulse on the map.
  - Action group completes when data packet transmission is confirmed.
- Status Draft
