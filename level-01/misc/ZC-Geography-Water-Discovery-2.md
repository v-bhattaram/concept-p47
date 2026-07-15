# ZC-Geography-Water-Discovery-2

## ActionGroup
- **ActionGroupName:** ZC-Geography-Water-Discovery-2
- **ActionType:** SideQuest
- **Level:** Level-01
- **Location:** Sector South — River Crossing
- **MarkerVisibility:** On ZC-GetDrone Complete
- **PreReqTrigger:** On ZC-GetDrone Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Drone Detects Water Source
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No — map marker appears labeled "Water Source — Unconfirmed"
- **BGMusic:** Ambient — brief curiosity note, water sound in the distance when approaching
- **Dialogs:**
  - SURD: Drone detected a water source while scanning. River system, approximately forty meters across. Sector South.
  - Player: Natural water.
  - SURD: Do not.
  - Player: I know. We scan it first.
  - SURD: I was going to say do not get excited. But scanning first is also correct.
- **Objectives:**
  - Ride to the river location in Sector South
- **GameplayNotes:**
  - SURD spots river while doing routine environmental scan
  - First natural water body the player can reach.
  - River is visually appealing — clear, fast-flowing, alien vegetation along the banks.
  - Player cannot collect water before scanning.
- Status Draft

---

### Trigger:Attempt Water Scan
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** River sound — flowing water, alien bird-like calls, peaceful surface over dangerous biology
- **Dialogs:**
  - Player: It looks clean.
  - SURD: Run the scan before that sentence finishes.
  - Player: Running.
  - SURD: I will overlay the biological analysis.
- **Objectives:**
  - Scan the river water using the suit scanner
- **GameplayNotes:**
  - player at river bank
  - Scan takes 10 seconds at the river bank.
  - Player cannot collect any water until scan completes.
- Status Draft

---

### Trigger:Analysis Results
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No — HUD shows scan results, red indicators
- **BGMusic:** Alert tone — not danger, but confirmation of negative result
- **Dialogs:**
  - SURD: As expected. Unknown biological compounds. Microfauna in concentrations that would cause rapid systemic failure.
  - Player: So the whole river is lethal.
  - SURD: Immediately and thoroughly, yes.
  - Player: It looks completely safe.
  - SURD: Most things that kill you do.
- **Objectives:**
  - Review scan results
- **GameplayNotes:**
  - scan finishes
  - If player attempts to manually collect water without scanning first: penalty applied. Minor health or suit damage.
  - This reinforces the scan-first discipline permanently.
- Status Draft

---

### Trigger:Log for Future Reference
- Trigger Type -> SideQuest
- Order 4
- **Cinematic:** No
- **BGMusic:** Ambient — thoughtful, a resource withheld but not lost
- **Dialogs:**
  - Player: But if we had a purification unit—
  - SURD: Theoretical. We do not have one.
  - Player: Log the location anyway.
  - SURD: Done. Marked for future reference. River designated: contaminated, natural water source, Planet 47 biology.
  - Player: Future reference. Meaning Level 2 or later, we might be able to use it.
  - SURD: Possibly. If you survive long enough to build the purification equipment.
  - Player: Thanks for the vote of confidence.
  - SURD: I am being accurate, not optimistic.
- **Objectives:**
  - Confirm river location is saved to map
- **GameplayNotes:**
  - Side quest complete. River location saved as "Contaminated Water Source — Purification Required."
  - This is a forward-looking marker — purification equipment is a future game unlock, not Level 1.
  - Player understands that natural resources are here, but they are not yet accessible. Reinforces the Zegas container dependency.
- Status Draft
