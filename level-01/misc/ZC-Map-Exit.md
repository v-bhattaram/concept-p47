# ZC-Map-Exit

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:Reach the Exit Marker
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Ride ambient — open terrain, forward momentum, understated
- **Dialogs:**
  - SURD: Transit zone ahead. Two kilometers.
  - Player: I see the marker.
- **Objectives:**
  - Ride the Manifest Bike to the map exit marker in Sector Northeast
- **GameplayNotes:**
  - Clear route, no enemies. The ride gives the player a final look at Level 1 terrain.
  - Bike is the right choice here — speed and open ground.
- Status Draft

---

### Trigger:Arrival
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** Partial — player dismounts at the edge of the transit zone. Brief pause. The crash site is visible in the far distance behind them.
- **BGMusic:** Music pauses — ambient only, wind, alien sounds
- **Dialogs:**
  - Player: This is it.
  - SURD: Level 1 operational chain complete. Energy Tower, MATREX, MIRA, LIRA. All active.
  - Player: No crew found.
  - SURD: No data on crew either.
  - Player: Not even bodies.
  - SURD: That question is not answered yet.
- **Objectives:**
  - Hold at the exit marker
- **GameplayNotes:**
  - player reaches exit marker, dismounts
  - This is a quiet reflective beat before the transition.
  - The absence of crew remains unresolved — intentional.
- Status Draft

---

### Trigger:Final Summary
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Low, thoughtful ambient — slight sense of forward movement starting
- **Dialogs:**
  - Player: And someone was already here. Ten to eighteen years before us.
  - SURD: MIRA confirmed it. Orbital Command confirmed it is real and told us to drop it.
  - Player: But they are not telling us who.
  - SURD: Not yet.
  - Player: And we are not alone. Not the creatures.
  - SURD: Also not yet explained.
  - Player: We have a lot of questions for Level 2.
  - SURD: We also have a bike, a working weapon, and a drone that talks too much.
  - Player: That last part is accurate.
  - SURD: Regret logged. Let's move.
- **Objectives:**
  - Activate the transit zone
- **GameplayNotes:**
  - Final SURD summary recaps what was accomplished and what remains open.
  - Bittersweet tone — survival achieved, mystery deepened.
- Status Draft

---

### Trigger:Level Transition
- Trigger Type -> Cutscene
- Order 4
- **Cinematic:** Yes — transit zone activates. White-out or fade to black. "Level 1 Complete" screen with stats summary. Then cut to Level 2 opening.
- **BGMusic:** Level complete sting, then fade to silence for Level 2 intro
- **Dialogs:** None
- **Objectives:** None
- **GameplayNotes:**
  - player activates transit zone
  - Show level stats: minerals collected, creatures encountered, side quests completed, optional quests completed, food/water found.
  - Transition to Level 2.
- Status Draft
