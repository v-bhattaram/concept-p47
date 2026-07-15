# ZC-Geography-Cliff-Discovery-1

## ActionGroup
- **ActionGroupName:** ZC-Geography-Cliff-Discovery-1
- **ActionType:** SideQuest
- **Level:** Level-01
- **Location:** Sector Northeast — Cliff Edge Overlook
- **MarkerVisibility:** On ZC-GetBike Complete
- **PreReqTrigger:** On ZC-GetBike Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:SURD Flags Elevation Point
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Open ambient — lighter tone, bike available, sense of possibility
- **Dialogs:**
  - SURD: Cliff edge to the northeast. Significant elevation. I recommend a terrain scan from there.
  - Player: Why?
  - SURD: Elevation advantage gives the drone better range and reduces atmospheric scatter. Best scan we can do without LIRA.
  - Player: And it costs nothing.
  - SURD: Correct.
- **Objectives:**
  - Ride the Manifest Bike to the cliff edge marker in Sector Northeast
- **GameplayNotes:**
  - quest marker appears
  - Bike route — open terrain, no creature zones blocking this path.
  - Cliff is a natural feature at the map's northeast edge.
- Status Draft

---

### Trigger:Survey the Landscape
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** Partial — brief wide shot of Planet 47's terrain from the cliff. Vast, strange, alien. The crash site is visible far behind in the southwest.
- **BGMusic:** Ambient swell — wide open, slightly awe-inspiring, alien wind at elevation
- **Dialogs:**
  - Player: This planet is enormous.
  - SURD: Planet 47 is roughly 1.4 times the diameter of the Zegas home world. You were not meant to be here.
  - Player: Thanks for the reminder.
- **Objectives:**
  - Stand at the cliff edge observation point
- **GameplayNotes:**
  - player reaches cliff edge, dismounts
  - Visual payoff moment. Player sees the scale of the planet for the first time at elevation.
  - Level 1 crash zone is visible in the far distance.
- Status Draft

---

### Trigger:Drone Long-Range Scan
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No — drone rises above cliff height, scan sweeps across the distant northeastern sector
- **BGMusic:** Scan tone — longer range, slower pulse than previous scans
- **Dialogs:**
  - SURD: Running long-range terrain scan. Range limit is approximately twelve kilometers at this altitude.
  - Player: What are you looking for?
  - SURD: Everything. Creature densities, water sources, crash material.
  - SURD: Contact. Wreckage signature in the far northeastern sector. Scale is significant.
  - Player: Another part of the armada?
  - SURD: Possibly. Scale and debris pattern do not fully match Zegas armada specifications.
- **Objectives:**
  - Drone scans far northeastern sector (automated)
- **GameplayNotes:**
  - player at cliff edge
  - Scan reveals: a second, large-scale wreckage site far to the northeast. Too distant to identify clearly.
  - This is a deliberate mystery seed — the wreckage is not Zegas Corp.
- Status Draft

---

### Trigger:Distant Site Logged
- Trigger Type -> SideQuest
- Order 4
- **Cinematic:** No — new map marker appears far northeast, labeled "Unknown Wreckage"
- **BGMusic:** Discovery tone, then thoughtful ambient
- **Dialogs:**
  - Player: You are saying it might not be ours.
  - SURD: I am saying the data does not confirm it is. The debris distribution pattern and structural scale are different from Zegas armada modules.
  - Player: Log it. I want that on the map.
  - SURD: Done. Marked as unknown wreckage. We should investigate when we have a route.
  - Player: After we have comms. After we have extraction. One thing at a time.
  - SURD: Logged in priority order.
- **Objectives:**
  - Confirm unknown wreckage marker is added to map
- **GameplayNotes:**
  - scan contacts confirmed
  - Side quest complete. "Unknown Wreckage" marker added to map in far northeast.
  - This is a Level 2 preview — the player will reach this site in a later level.
  - The wreckage is Syntara Prime, but this is not stated.
- Status Draft
