# ZC-Weapons-Crafting

## ActionGroup
- **ActionGroupName:** ZC-Weapons-Crafting
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Alpha — Field Fabricator
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Energy-Crystals-Intro Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Creature Pressure Increases
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — creature audio closer than before, shadows moving between wreckage in the background
- **BGMusic:** Tension rise — creature proximity cues layered under ambient
- **Dialogs:**
  - Player: I need something between me and those teeth.
  - SURD: Crafting recommendation: emergency pulse cutter.
  - Player: Is it a weapon?
  - SURD: Zegas classification: industrial tool.
  - Player: Does it stop creatures?
  - SURD: Temporarily.
  - Player: Then it is a weapon today.
- **Objectives:**
  - Locate the field fabricator
- **GameplayNotes:**
  - Creatures are visibly getting bolder near the crash zone. Player still has no weapon.
  - Creates urgency to reach the fabricator fast.
- Status Draft

---

### Trigger:Repair Field Fabricator
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — fabricator powers on with a low hum when crystals inserted
- **Dialogs:**
  - SURD: Fabricator is damaged but repairable. Insert energy crystals to restore power.
  - Player: Same crystals I just collected.
  - SURD: Multi-use resource. You will be depending on them for most of your systems.
- **Objectives:**
  - Insert energy crystals to power the field fabricator (3 crystals)
- **GameplayNotes:**
  - player reaches fabricator
  - Fabricator starts up. UI opens when powered.
  - Power cost: 3 stable crystals from inventory.
- Status Draft

---

### Trigger:Gather Weapon Materials
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Ambient — urgency note maintained
- **Dialogs:**
  - SURD: You need alloy fragments, conduit minerals, and two stable energy crystals to fabricate the pulse cutter.
  - Player: I have the minerals from before. I need the rest.
  - SURD: Alloy fragments are in the nearest cargo stack. Be fast.
- **Objectives:**
  - Collect alloy fragments from the cargo stack (2 units)
  - Confirm conduit minerals are in inventory (from ZC-Minerals-Intro)
  - Confirm stable energy crystals are in inventory (from ZC-Energy-Crystals-Intro)
- **GameplayNotes:**
  - fabricator online
  - Player should already have conduit minerals and crystals from earlier action groups.
  - Only new material to gather is the alloy fragments — short run to nearby cargo.
  - If materials are short, the fabricator UI shows what is missing.
- Status Draft

---

### Trigger:Craft Emergency Pulse Cutter
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** No — fabricator animation plays during crafting
- **BGMusic:** Fabrication sound effect — mechanical, building, then completion tone
- **Dialogs:**
  - SURD: Fabricating. Thirty seconds.
  - Player: (watches the perimeter)
  - SURD: Pulse cutter complete.
  - Player: Finally.
- **Objectives:**
  - Craft the emergency pulse cutter at the fabricator
- **GameplayNotes:**
  - all materials confirmed
  - Weapon is placed in inventory. Does not auto-equip — weapon equip is handled in ZC-Weapons-Unlock.
  - Weapons do not create a hunting loop. Alien creatures do not drop food or water.
  - Combat is for survival, defense, and clearing blocked routes only.
- Status Draft
