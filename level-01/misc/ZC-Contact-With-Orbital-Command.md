# ZC-Contact-With-Orbital-Command

## ActionGroup
- **ActionGroupName:** ZC-Contact-With-Orbital-Command
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Signal Peak — Comms Relay Site
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Planet47-Creatures2 Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Build Comms Relay
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Ambient — slightly more hopeful tone, wind at elevation (Signal Peak is higher ground)
- **Dialogs:**
  - SURD: Signal Peak is the best position. Minimal atmospheric interference compared to the crash valley.
  - Player: How far are we from Orbital Command?
  - SURD: Far enough that this relay will only get us a partial burst. But it is enough to confirm we are alive.
  - Player: That will have to do.
- **Objectives:**
  - Ride the Manifest Bike to Signal Peak
  - Assemble the temporary comms relay from collected components
- **GameplayNotes:**
  - player has all comms components
  - Player assembles relay using: broken comms panels, signal amplifier, and 3 stable energy crystals.
  - Relay assembly is a short interactive sequence — connect components in order.
- Status Draft

---

### Trigger:Align Signal
- Trigger Type -> ForcedPuzzle
- Order 2
- **Cinematic:** No
- **BGMusic:** Alignment tone — rising pitch as percentage climbs, steady when locked
- **Dialogs:**
  - SURD: Relay alignment at 41 percent. Atmospheric interference remains severe.
  - Player: Push it anyway.
  - SURD: I need a higher position for alignment. I will hover above the relay dish.
  - Player: Do it.
  - SURD: Alignment at 67 percent. Holding.
- **Objectives:**
  - SURD drone hovers over the relay to handle signal alignment
  - Hold position while alignment locks (do not move relay)
- **GameplayNotes:**
  - relay assembled
  - Player must stay near the relay — if they leave the zone, alignment drops.
  - This is a brief stationary moment before the transmission.
- Status Draft

---

### Trigger:First Contact
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** Yes — relay sparks to life, SURD drone glows brighter, static crackles through the relay speaker
- **BGMusic:** Static burst, then a moment of near-silence, then fragmented signal
- **Dialogs:**
  - SURD: Transmitting emergency burst.
  - Player: Orbital Command, this is Zegas survivor on Planet 47. Armada down. Do you read?
  - Orbital Command: ...Zegas... identify... signal weak...
  - Player: I am alive. SURD is active. We need extraction and survivor scan.
  - Orbital Command: ...course change... not authorized... stay alive... restore chain...
  - SURD: Signal lost.
  - Player: They heard us.
  - SURD: Partial contact confirmed.
- **Objectives:**
  - Transmit emergency identification
  - Receive partial response from Orbital Command
- **GameplayNotes:**
  - alignment locked at 67 percent or above
  - "Course change not authorized" is a deliberate mystery seed. The armada's crash was not accidental.
  - Milestone: First Orbital Contact achieved.
- Status Draft

---

### Trigger:Contact Outcome
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Quiet ambient — post-tension release, but the mystery lingers
- **Dialogs:**
  - Player: What does "restore chain" mean?
  - SURD: Operational chain. Zegas field protocol for establishing a working extraction site.
  - Player: Energy Tower, MATREX, MIRA, LIRA.
  - SURD: In that order. It is standard for any Zegas mining survey site. Orbital Command wants us to run the chain before they can route an extraction.
  - Player: And the course change? Someone moved our armada into this planet.
  - SURD: That is outside my current data.
  - Player: Noted.
- **Objectives:**
  - Understand the operational chain directive
- **GameplayNotes:**
  - transmission ends
  - Player now has a clear primary mission: run the operational chain.
  - The unauthorized course change is a story thread that will not be explained until later levels.
- Status Draft
