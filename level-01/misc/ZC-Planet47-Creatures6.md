# ZC-Planet47-Creatures6

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures6
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** LIRA-X9 Site — Sector North
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Operational-Chain-MIRA-Instructions Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Apex Predator at LIRA Site
- Trigger Type -> Story
- Order 1
- **Cinematic:** Partial — drone sends feed from distance. The LIRA-X9 tower is visible. An apex predator — significantly larger than anything encountered before — is directly in front of it, moving slowly, claiming the area.
- **BGMusic:** Heavy threat tone — lower and slower than previous creature encounters, signaling this is different
- **Dialogs:**
  - SURD: LIRA site is ahead. I am also detecting a large apex-class signature at the site.
  - Player: How large?
  - SURD: Larger than anything we have encountered.
  - Player: Can we go around?
  - SURD: No. The LIRA tower is inside its territory. There is no clear bypass path at this range.
- **Objectives:**
  - Observe the apex predator via drone feed
  - Assess available tools and environment
- **GameplayNotes:**
  - player approaches Sector North
  - This is the climax creature encounter of Level 1 — multi-phase, most difficult fight so far.
  - The creature cannot be killed outright. It must be stunned enough times or overloaded using environmental crystal clusters.
  - Unstable crystal clusters are visible near the tower site — these can be overloaded and triggered as area traps.
- Status Draft

---

### Trigger:Prepare the Approach
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Pre-combat planning tone — tense, deliberate
- **Dialogs:**
  - Player: Options?
  - SURD: Bike for speed. Drone for distraction. Weapon for direct damage. There are unstable crystal clusters near the tower site.
  - Player: You want me to use the crystals as traps.
  - SURD: I want you to survive. The crystals are a means to that end.
  - Player: Mark the cluster positions.
  - SURD: Marked. Approach from the west — the wind is coming from the east. It may reduce your scent signature.
  - Player: It has a scent signature detection?
  - SURD: Most apex predators do.
  - Player: Great detail to share now.
- **Objectives:**
  - Review crystal cluster positions on the HUD
  - Approach the LIRA site from the west
- **GameplayNotes:**
  - Player should dismiss the bike before entering combat range — noise detection.
  - Crystal clusters are marked on HUD. Triggering one requires a full-charge shot at close range.
- Status Draft

---

### Trigger:Combat — Force the Predator Back
- Trigger Type -> ForcedCombat
- Order 3
- **Cinematic:** No
- **BGMusic:** Full combat music — heaviest in Level 1, building intensity
- **Dialogs:**
  - SURD: It sees you. Engaging.
  - Player: Moving to the first cluster.
  - SURD: I will buzz the left flank. Draw its attention.
  - (combat sequence)
  - SURD: First hit. It is not retreating.
  - Player: Second cluster. Move.
  - SURD: On it.
  - (second hit)
  - Player: It is still coming.
  - SURD: Third cluster. Last one in range.
  - Player: If this does not work—
  - SURD: It will work.
- **Objectives:**
  - Stun the apex predator 3 times using weapon shots and crystal cluster detonations
  - Use drone to draw creature attention away from player between attacks
  - Avoid direct sustained melee — this creature kills in close quarters
- **GameplayNotes:**
  - player enters combat zone
  - Three-phase fight: each phase requires a stun hit (weapon or crystal).
  - Drone distraction pulls creature attention for 5 to 8 seconds per use — limited charges per encounter.
  - Crystal cluster detonation: full-charge shot at cluster = large area stun + knockback.
  - After 3 stuns the creature is damaged enough to retreat.
- Status Draft

---

### Trigger:Creature Retreats
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — apex predator stumbles, lets out a deep vocalization, and retreats northward into dense cover
- **BGMusic:** Combat music fades — long exhale ambient
- **Dialogs:**
  - Player: Go. Now. LIRA before it recovers.
  - SURD: Agreed. Quickly. I do not know how long it stays down.
- **Objectives:**
  - Move to the LIRA-X9 tower immediately
- **GameplayNotes:**
  - Trigger condition: Three stuns/detonations complete
  - Action group completes when player reaches the LIRA-X9 tower base.
  - Creature does not return during the LIRA activation sequence.
- Status Draft
