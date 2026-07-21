# ZC-Planet47-Creatures5

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures5
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** MIRA Station Approach — Dense Wreckage, Sector Central-West
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Operational-Chain-MATREX-Instructions Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:SURD Detects Territorial Behavior
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — drone scouts ahead and transmits a feed. A large, slow creature is resting against the MIRA station structure, fully claiming the area as its denning site.
- **BGMusic:** Ambient drops in energy — slow, heavy, territorial
- **Dialogs:**
  - SURD: MIRA station is in the next sector. There is a problem.
  - Player: Of course there is.
  - SURD: Large territorial predator. It has claimed the MIRA site as a denning area.
  - Player: Of course it has.
  - SURD: The good news is it is slow. The bad news is it is very large.
- **Objectives:**
  - Observe the MIRA site via drone feed
- **GameplayNotes:**
  - player approaches Sector Central-West
  - New creature type: large territorial ground predator. Slow but enormous. Not sensory — relies on close-range detection.
  - This creature cannot be fought effectively with current weapons — it is too large. Bypass is the only option.
- Status Draft

---

### Trigger:Drone Recon of Approach
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No — drone maps the site, reveals a low passage through dense wreckage on the south side
- **BGMusic:** Stealth ambient — low, careful
- **Dialogs:**
  - Player: Can the drone distract it?
  - SURD: I can lure it toward the ridge while you approach from the low side. The creature reacts to movement and heat.
  - Player: The drone puts out heat?
  - SURD: Enough at close range. I will make it worth its time.
  - Player: I do not recommend thinking about that sentence too long.
  - SURD: Agreed. Ready when you are.
- **Objectives:**
  - Use drone to map the low south passage to the MIRA station
  - Confirm lure point and approach route
- **GameplayNotes:**
  - Drone reveals: low wreckage passage on south side, creature lure point on the ridge northwest.
  - Player must be on foot — the passage is too narrow for the bike.
- Status Draft

---

### Trigger:Distract and Bypass
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Tension stealth track — held breath, slow pulse
- **Dialogs:**
  - SURD: Moving toward lure point now.
  - Player: I will move when the creature turns.
  - SURD: You will have forty seconds once it commits to the ridge.
  - Player: That is enough.
- **Objectives:**
  - Wait for SURD to lure the creature to the ridge
  - Advance through the low south passage on foot (40 seconds)
  - Reach the MIRA station entrance before the creature returns
- **GameplayNotes:**
  - player ready at passage entrance
  - Timed stealth sequence. Creature turns away when drone reaches lure point.
  - If player is too slow or makes noise: creature returns, detects player, player must sprint out and reset.
  - No fail state — just a reset. The sequence can be retried.
- Status Draft

---

### Trigger:Reach MIRA Station
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Brief exhale tone, then MIRA station ambient — electronic hum, powered systems
- **Dialogs:**
  - Player: Inside. Go.
  - SURD: (from outside) Creature is returning. I am moving to the station exterior. Safe distance.
  - Player: Get clear. I have it from here.
- **Objectives:**
  - Enter the MIRA station
- **GameplayNotes:**
  - player inside MIRA station entrance
  - Creature returns to its den position but does not enter the station.
  - Player is safe inside.
  - Action group completes when player crosses the MIRA station threshold.
- Status Draft
