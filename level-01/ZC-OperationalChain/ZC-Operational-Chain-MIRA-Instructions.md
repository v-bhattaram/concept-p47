# ZC-Operational-Chain-MIRA-Instructions

## ActionGroup
- **ActionGroupName:** ZC-Operational-Chain-MIRA-Instructions
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** MIRA Station — Sector Central-West
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Planet47-Creatures5 Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Activate MIRA Terminal
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No — MIRA terminal screen activates when player approaches, powered by the Energy Tower
- **BGMusic:** MIRA station ambient — data processing hum, clean electronic sounds
- **Dialogs:**
  - Player: MIRA. Last one before LIRA.
  - SURD: (from exterior) Terminal should be live. Energy Tower power is reaching this station.
  - Player: It is on. Coming in now.
- **Objectives:**
  - Activate the MIRA terminal
- **GameplayNotes:**
  - player inside MIRA station
  - MIRA terminal is already powered (Energy Tower feeds it). Player just needs to interface.
  - MIRA System: Material Intelligence and Reporting Assistant.
- Status Draft

---

### Trigger:Load MATREX Data Packet
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — data transfer animation on screen
- **BGMusic:** Transfer sequence — rapid data sound, progress indicator tone
- **Dialogs:**
  - SURD: Load the MATREX data packet first. It is already in your suit's relay buffer.
  - Player: Uploading now.
  - MIRA System: MATREX extraction report received. Processing site data.
  - SURD: Good. Now load the survey data from your scans.
- **Objectives:**
  - Transfer the MATREX data packet to MIRA (automatic from suit buffer)
- **GameplayNotes:**
  - MIRA terminal active
  - Automatic transfer — no extra materials needed. Suit holds the packet from MATREX.
- Status Draft

---

### Trigger:Load Planet Survey Data
- Trigger Type -> ForcedPuzzle
- Order 3
- **Cinematic:** No
- **BGMusic:** Data processing audio continues
- **Dialogs:**
  - Player: Loading all scan data. Mineral scans, creature scans, geography scans. Everything.
  - SURD: MIRA builds a planetary profile. The more it has, the stronger the LIRA signal.
  - Player: So everything I scanned actually mattered.
  - SURD: It always mattered. Now it has a destination.
- **Objectives:**
  - Upload all player scan data to MIRA (minerals, creatures, geography — everything collected this level)
- **GameplayNotes:**
  - MATREX data loaded
  - Retroactively rewards thorough scanning throughout Level 1.
  - Players who completed creature and geography side quests get higher MIRA data quality.
  - Upload volume affects LIRA signal strength — higher quality gives a faster LIRA alignment time.
- Status Draft

---

### Trigger:MIRA Flags Anomaly
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — MIRA terminal screen flashes an alert flag, highlighted in a distinct color
- **BGMusic:** Alert tone — not dangerous, but significant. Data discovery sound.
- **Dialogs:**
  - MIRA System: Data load complete. Survey data integrated. Planetary profile generated. One anomaly flagged.
  - Player: What anomaly?
  - MIRA System: Prior mineral extraction activity detected. Estimated period: twelve to eighteen years ago.
  - SURD: (entering through exterior door) That predates our armada by over a decade.
  - Player: Someone was already here.
  - SURD: Unknown operator. MIRA cannot identify the source from extraction pattern alone.
  - Player: But someone extracted minerals from this planet before we got here.
  - SURD: That is what the data says.
  - Player: And Orbital Command told us not to investigate.
  - SURD: I noticed that too.
- **Objectives:**
  - Review MIRA anomaly flag
- **GameplayNotes:**
  - data upload complete
  - Story seed for Syntara Prime — do not name them yet. Player will discover who it was in Level 2.
  - SURD re-enters the station here — the territorial creature has returned to its den but is not blocking the door.
- Status Draft

---

### Trigger:MIRA Enables LIRA
- Trigger Type -> ForcedQuest
- Order 5
- **Cinematic:** No — LIRA-X9 marker pulses on the map
- **BGMusic:** System handoff tone — MIRA to LIRA link confirmed
- **Dialogs:**
  - MIRA System: Data processing complete. LIRA-X9 access authorized.
  - SURD: LIRA marker is active. Sector North.
  - Player: How do we get past the territorial creature outside?
  - SURD: It moved. I will explain outside.
- **Objectives:**
  - Confirm LIRA-X9 access is authorized
  - Exit MIRA station
- **GameplayNotes:**
  - MIRA data loaded = Touch Point achieved.
  - LIRA-X9 marker activates on the map.
  - Creature has moved away from the station entrance — player can exit safely.
- Status Draft
