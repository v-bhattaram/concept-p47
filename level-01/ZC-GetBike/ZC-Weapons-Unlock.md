# ZC-Weapons-Unlock

## ActionGroup
- **ActionGroupName:** ZC-Weapons-Unlock
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Debris Field Alpha — Field Fabricator
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Weapons-Crafting Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Safety Unlock Granted
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** No — weapon equip slot activates on HUD
- **BGMusic:** Short system unlock tone
- **Dialogs:**
  - SURD: Weapon system unlocked under emergency survival clause.
  - Player: You had that clause ready fast.
  - SURD: You encountered carnivorous megafauna before breakfast.
  - Player: Fair.
  - SURD: Reminder. This tool is for defense and route clearance.
  - Player: Noted. I am not hunting dinner here.
- **Objectives:**
  - Equip the pulse cutter from inventory
- **GameplayNotes:**
  - Weapon equip slot unlocks on the HUD.
  - Zegas corporate weapons are restricted systems — SURD authorizes under emergency clause.
- Status Draft

---

### Trigger:Weapon Tutorial
- Trigger Type -> ForcedQuest
- Order 2
- **Cinematic:** No
- **BGMusic:** Ambient — no change
- **Dialogs:**
  - SURD: Standard functions: aim, charge shot, stun pulse, and cooldown. Do not fire while cooling.
  - Player: What is the cooldown period?
  - SURD: Eight seconds at full charge. Four at half charge.
  - Player: So aim properly.
  - SURD: That would be ideal.
- **Objectives:**
  - Learn aim and fire controls
  - Learn charge shot mechanic
  - Understand cooldown display on HUD
- **GameplayNotes:**
  - weapon equipped
  - Full tutorial overlay for weapon controls. Displayed once.
  - Half charge: stun effect, fast cooldown. Full charge: knockback + stun, longer cooldown.
- Status Draft

---

### Trigger:Test Fire on Debris
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No
- **BGMusic:** Weapon discharge sound effect — clean, industrial
- **Dialogs:**
  - SURD: Test fire on the damaged plating to the left.
  - Player: (fires)
  - SURD: Charge level confirmed. Aim calibration complete.
- **Objectives:**
  - Fire the pulse cutter at the marked debris plating
- **GameplayNotes:**
  - Target is a fixed piece of wreckage, not a creature.
  - Demonstrates visual and physics feedback from the weapon.
- Status Draft

---

### Trigger:First Creature Defense
- Trigger Type -> ForcedCombat
- Order 4
- **Cinematic:** Partial — small predator moves toward the player from behind wreckage
- **BGMusic:** Short tension spike, then release when creature backs off
- **Dialogs:**
  - SURD: Small predator approaching. This is a good test.
  - Player: A test. Right.
  - (player fires stun shot)
  - SURD: Creature deterred. Moving away.
  - Player: Okay. That works.
  - SURD: Return to the Type-P search route.
- **Objectives:**
  - Stun or scare off the small creature
  - Resume the Type-P search route
- **GameplayNotes:**
  - small creature enters the area
  - Creature is not killed, just stunned or scared off. Reinforces the defense-only combat philosophy.
  - Unlocks: defensive combat tutorials, full weapon use for the rest of the level.
- Status Draft
