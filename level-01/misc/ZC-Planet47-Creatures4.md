# ZC-Planet47-Creatures4

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures4
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Energy Tower Site — Perimeter
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Operational-Chain-Energy-Tower-Instructions Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Aerial Contacts Detected
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — SURD drone spins upward, scanning. Shadow passes over the tower. Camera tilts up briefly to show fast-moving aerial creatures banking toward the energy signature from the ridge.
- **BGMusic:** New threat tone — faster, higher pitch than ground creatures, urgent
- **Dialogs:**
  - SURD: Energy signature confirmed. Also confirmed: it is visible to everything within two kilometers.
  - Player: How many?
  - SURD: Three aerial contacts. Fast. Coming from the ridge.
  - Player: Those things can fly.
  - SURD: Glide. Technical distinction. Still dangerous.
- **Objectives:**
  - Assess the incoming aerial threat
- **GameplayNotes:**
  - immediately after tower activation
  - New creature type introduced: aerial gliders. Fast, low armor, attack in coordinated passes. Travel in packs of 2 to 3.
  - Unlike ground creatures, they cannot be outrun on foot. Bike in open terrain is an option for evasion.
- Status Draft

---

### Trigger:Defend Tower Perimeter
- Trigger Type -> ForcedCombat
- Order 2
- **Cinematic:** No
- **BGMusic:** Combat music — faster tempo than previous encounters, aerial movement sounds
- **Dialogs:**
  - Player: Stun one. Scatter the rest. Keep the tower running.
  - SURD: Their attack pattern is dive-and-retreat. Lead the shot.
  - Player: Lead the shot. Right.
- **Objectives:**
  - Defend the Energy Tower perimeter
  - Stun or deter aerial creatures before they damage the tower or the drone
  - Player and drone work together — drone handles distraction, player handles shots
- **GameplayNotes:**
  - creatures enter attack range
  - Aerial creatures move faster than ground threats. Full charge shot has wider spread — more effective against airborne targets.
  - Drone distraction pulls one creature off course for 5 seconds per use.
  - Tower is not destroyable in this encounter — this is a combat teaching moment, not a fail-state defense.
- Status Draft

---

### Trigger:Pack Retreats
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No — creatures bank away and disappear over the ridge
- **BGMusic:** Combat music fades to ambient — victory without triumph
- **Dialogs:**
  - SURD: They are retreating. Pack behavior. One stunned, others disengaged.
  - Player: MATREX. Now.
  - SURD: Agreed. Before anything else finds the power signature.
- **Objectives:**
  - Confirm all aerial creatures have left the perimeter
- **GameplayNotes:**
  - Trigger condition: One creature stunned and remaining creatures disengage
  - Creatures do not drop items. No creature meat or harvest.
  - Player now knows aerial threats exist and are attracted to active Zegas energy systems.
  - Action group completes when perimeter is clear. Player rides toward MATREX.
- Status Draft
