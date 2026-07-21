# ZC-Planet47-Creatures2

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures2
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Beta — Armored Creature Territory
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-GetDrone Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Drone First Scout
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — drone detaches and moves ahead of the player
- **BGMusic:** Drone flight sound — steady hum, slight shift in ambient as drone moves forward
- **Dialogs:**
  - SURD: Movement detected ahead. Larger creature. Heavy exterior plating.
  - Player: Can your drone shoot it?
  - SURD: Yes. Ineffectively.
  - Player: Recon it is.
  - SURD: Sensible choice.
- **Objectives:**
  - Send SURD's drone ahead to scout the wreckage field
- **GameplayNotes:**
  - player moves toward next wreckage field
  - First drone scouting tutorial. Player activates drone scout from the suit interface.
  - Drone moves autonomously into the danger zone and transmits a feed to the player's HUD.
- Status Draft

---

### Trigger:Mark Patrol Routes
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — map overlay updates with creature patrol path
- **BGMusic:** Ambient — tension sustained while creature is visible on drone feed
- **Dialogs:**
  - SURD: One armored creature. Patrol circuit covers the central passage and the east debris pile.
  - Player: How long is the circuit?
  - SURD: Forty seconds per loop. There is a gap on the west side.
  - Player: That is the way through.
  - SURD: Correct.
- **Objectives:**
  - Mark creature patrol routes using the drone feed (3 route points)
- **GameplayNotes:**
  - drone completes initial sweep
  - Creature is a new type: large, heavily armored, ground-based. Slow but powerful.
  - Drone scan reveals: this creature is heat-blind, detects vibration and ground movement instead.
  - Route markers appear on the player's map automatically from the drone scan.
- Status Draft

---

### Trigger:Slip Past the Armored Creature
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Stealth ambient — low pulse tied to creature proximity
- **Dialogs:**
  - SURD: Wait for the creature to reach the east pile. Move through the west gap. On foot — the bike creates too much vibration.
  - Player: On foot through armored creature territory. Perfect.
  - SURD: I will alert you if it changes route.
- **Objectives:**
  - Wait for patrol gap
  - Advance on foot through the west passage (bike dismissed before entering)
  - Reach the far side without triggering the armored creature
- **GameplayNotes:**
  - patrol routes mapped
  - Bike must be dismissed before entering this zone. Vibration detection = bike is detected immediately.
  - Teaches selective use of bike vs. on-foot movement.
  - If detected: creature charges. Player must run out of the zone, not fight it. Weapon is ineffective against heavy plating.
- Status Draft

---

### Trigger:Recover Signal Amplifier
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Brief relief note, then ambient returns
- **Dialogs:**
  - Player: What is a signal amplifier doing out here?
  - SURD: It is from one of the comms modules. Still functional.
  - Player: Enough to reach Orbital Command?
  - SURD: Combined with what we have already found, possibly.
- **Objectives:**
  - Collect the signal amplifier from the debris stack
- **GameplayNotes:**
  - player clears the creature zone
  - Signal amplifier is the last component needed for the comms relay in ZC-Contact-With-Orbital-Command.
  - Action group completes when amplifier is picked up and player exits Debris Field Beta.
- Status Draft
