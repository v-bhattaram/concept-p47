# ZC-Creature-Discover-2

## ActionGroup
- **ActionGroupName:** ZC-Creature-Discover-2
- **ActionType:** SideQuest
- **Level:** Level-01
- **Location:** Wreckage Path — Armored Creature Zone
- **MarkerVisibility:** On ZC-Planet47-Creatures1 Complete
- **PreReqTrigger:** On ZC-Planet47-Creatures1 Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Track Without Engaging
- Trigger Type -> SideQuest
- Order 1
- **Cinematic:** No
- **BGMusic:** Stealth ambient — low, careful, deliberate
- **Dialogs:**
  - SURD: The armored creature has a patrol route. If we track it without engaging, I can map its behavior pattern.
  - Player: What for?
  - SURD: Future encounters. Understanding how it hunts gives us an advantage.
  - Player: Fine. I am following a thing that wants to eat me for science.
  - SURD: For survival. Science is secondary.
- **Objectives:**
  - Follow the armored creature's patrol route without being detected (3 patrol checkpoints)
- **GameplayNotes:**
  - quest marker appears
  - Player follows at a safe distance. Stay behind cover at each checkpoint.
  - This creature detects vibration — no running, no bike. On foot only.
- Status Draft

---

### Trigger:Drone Behavior Analysis
- Trigger Type -> SideQuest
- Order 2
- **Cinematic:** No — drone analysis overlay activates
- **BGMusic:** Analysis scan tone — methodical, building toward discovery
- **Dialogs:**
  - SURD: Running behavior pattern analysis. Hold position at the third checkpoint.
  - Player: (holds)
  - SURD: Interesting. It is not reacting to temperature or light. Only to ground contact.
  - Player: It is completely heat-blind.
  - SURD: Correct. It detects by vibration and ground movement. Body heat, light, and airborne scent are irrelevant.
- **Objectives:**
  - Hold at the final checkpoint while SURD runs drone behavior analysis
- **GameplayNotes:**
  - all 3 checkpoints tracked
  - This is a passive hold — player just waits 15 seconds while SURD processes.
  - Reveals a critical tactical note: this creature type cannot detect the player if they stand still on solid ground, but running or bike use is immediately detected.
- Status Draft

---

### Trigger:Catalog Entry 2 Unlocked
- Trigger Type -> SideQuest
- Order 3
- **Cinematic:** No — catalog entry 2 populates
- **BGMusic:** Discovery tone
- **Dialogs:**
  - SURD: Catalog entry 2 complete. Armored ground predator. Detection: vibration only. Heat-blind. Light-blind. Vulnerability: none confirmed at current weapon level.
  - Player: None confirmed.
  - SURD: Not with a pulse cutter. Better weapons in a future level, possibly.
  - Player: Add it to the list of reasons to survive.
  - SURD: Strategy note added: on foot only in armored creature zones. Bike creates detectable ground vibration at range.
- **Objectives:**
  - Review catalog entry 2
- **GameplayNotes:**
  - Side quest complete. Catalog entry 2 includes: behavior pattern map for this specific creature, patrol route length, detection method.
  - Tactical note added to map: armored creature zones marked as "no bike" areas.
- Status Draft
