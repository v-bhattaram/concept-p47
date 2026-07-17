# ZC-Operational-Chain-Energy-Tower-Instructions

## LocationGroup = FolderName
## Location = File Name
## Location Actions/toDos = Trigger (3 pound ### entries in file name)

---
### Trigger:Locate the Energy Tower
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — camera briefly shows the Energy Tower in the distance: tall, battered, still standing above the tree line
- **BGMusic:** Ambient — open terrain ride music, steady forward movement
- **Dialogs:**
  - Player: This tower survived the crash better than anything else.
  - SURD: Zegas reinforced infrastructure. It was built to survive exactly this.
  - Player: Surviving the crash isn't impressive anymore. Let's open it.
- **Objectives:**
  - Ride the Manifest Bike to Energy Tower — Sector East
  - Clear any obstacles on the approach path
- **GameplayNotes:**
  - player rides toward Sector East
  - Energy Tower is a Zegas standard field installation — tall power distribution unit.
  - Approach path may have debris or wandering creature that player needs to avoid or bypass on bike.
- Status Draft

---

### Trigger:Bypass Security Lock
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — steady, waiting
- **Dialogs:**
  - SURD: Security lock is damaged but active. Give me a moment.
  - Player: The wildlife is going to notice the power signature when this comes on.
  - SURD: Faster is better.
  - SURD: Override sequence running. Access panel will open in ten seconds.
- **Objectives:**
  - Allow SURD to run bypass override (10-second wait, stay near the tower)
- **GameplayNotes:**
  - player reaches the tower base
  - SURD interfaces with the tower via the drone.
  - Player stays at the base. This is a brief stationary moment.
  - Creature audio begins in the background — low, distant, not yet a threat.
- Status Draft

---

### Trigger:Restore Power Feed
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Tower power-up sequence — deep mechanical sound, growing hum
- **Dialogs:**
  - SURD: Tower core is open. Insert energy crystals into the power feed ports. All three ports.
  - Player: Three crystals for a whole tower?
  - SURD: It seeds the chain reaction. The tower extracts ambient crystal energy from the local geology after that.
  - Player: It keeps itself running?
  - SURD: Once started. Yes.
- **Objectives:**
  - Insert stable energy crystals into all three power feed ports (3 crystals)
- **GameplayNotes:**
  - access panel opens
  - Consumes 3 stable crystals from inventory.
  - Each port lights up as crystal is inserted. Third port triggers the tower activation sequence.
- Status Draft

---

### Trigger:Tower Online
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Yes — Energy Tower powers up with a deep resonance. Lights climb from base to top. A visible energy pulse radiates outward. MATREX station marker lights up on the HUD.
- **BGMusic:** Power surge — grand, building, then settling into a strong operational hum
- **Dialogs:**
  - SURD: Energy Tower online. MATREX systems are now receiving power.
  - Player: Good. Where is MATREX?
  - SURD: Sector Central. Already marked.
  - Player: Then we move.
- **Objectives:**
  - Confirm tower is online
  - Check MATREX marker on map
- **GameplayNotes:**
  - third crystal inserted
  - Energy Tower online = Touch Point achieved.
  - MATREX marker activates on map.
  - Creature encounter ZC-Planet47-Creatures4 triggers immediately after this action group.
- Status Draft
