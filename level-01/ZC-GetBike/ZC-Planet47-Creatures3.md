# ZC-Planet47-Creatures3

## ActionGroup
- **ActionGroupName:** ZC-Planet47-Creatures3
- **ActionType:** StoryLine
- **Level:** Level-01
- **Location:** Signal Peak — Comms Relay Site
- **MarkerVisibility:** Always On
- **PreReqTrigger:** On ZC-Contact-With-Orbital-Command Complete
- **ActionGroupStatus:** Active

---

## ActionItems

### Trigger:Signal Attracts Creature
- Trigger Type -> ForcedQuest
- Order 1
- **Cinematic:** Partial — SURD drone spins toward the ridge. Camera briefly shows a large creature emerging from tree line, drawn by the energy and heat signature of the relay.
- **BGMusic:** Sudden stinger — threat tone, urgent
- **Dialogs:**
  - SURD: Large hostile approaching.
  - Player: Of course the first good signal rings the dinner bell.
  - SURD: Reminder. You are not dinner.
  - Player: Tell that to the creature.
- **Objectives:**
  - Prepare to defend the relay site
- **GameplayNotes:**
  - immediately after transmission ends
  - Creature is drawn by the combined energy signature of the relay, crystals, and drone.
  - This is the first high-threat creature encounter — larger and more aggressive than anything seen so far.
- Status Draft

---

### Trigger:Hold the Relay
- Trigger Type -> ForcedCombat
- Order 2
- **Cinematic:** No
- **BGMusic:** Combat music — urgent, percussive, with electronic elements
- **Dialogs:**
  - SURD: I need thirty seconds to save the transmission log. Keep it away from the relay.
  - Player: Thirty seconds.
  - SURD: Do not let it destroy the relay. The data goes with it if it does.
- **Objectives:**
  - Defend the comms relay for 30 seconds while SURD saves the transmission log
  - Use drone distraction to create openings
  - Stun the creature or force it away from the relay
- **GameplayNotes:**
  - Player uses weapon, drone support, and debris cover in combination.
  - Drone can buzz the creature to redirect its attention for 5 to 8 seconds.
  - Relay is a destructible object — if creature reaches it, the transmission log is lost (fail state).
  - Full charge stun pushes the creature back. Half charge only slows it.
- Status Draft

---

### Trigger:Transmission Log Saved
- Trigger Type -> ForcedQuest
- Order 3
- **Cinematic:** No — SURD audio confirms save
- **BGMusic:** Brief beat change — urgency peaks, then drops
- **Dialogs:**
  - SURD: Transmission log saved. We can leave.
  - Player: Bike. Now.
- **Objectives:**
  - Break off and reach the Manifest Bike
- **GameplayNotes:**
  - Trigger condition: 30 seconds elapsed and relay intact
  - Player does not need to kill the creature. Leaving the combat zone is the win condition.
  - Bike summon point is 20 m from the relay site — player must sprint there.
- Status Draft

---

### Trigger:Escape on Bike
- Trigger Type -> ForcedQuest
- Order 4
- **Cinematic:** Partial — player mounts bike and accelerates away from Signal Peak, creature charges behind and then stops at the tree line
- **BGMusic:** Engine acceleration, then open terrain ambient as creature gives up pursuit
- **Dialogs:**
  - Player: (while riding) Is that it?
  - SURD: It stopped at the tree line. Territorial boundary.
  - Player: They have territories.
  - SURD: Established behavior. We now know Signal Peak is inside that one's range.
  - Player: Good to know. Where are we going?
  - SURD: Somewhere with less creature interest and more working Zegas infrastructure.
- **Objectives:**
  - Escape the creature on the Manifest Bike
  - Reach the safe zone outside the creature's territory
- **GameplayNotes:**
  - player reaches bike summon point
  - Action group completes when player exits Signal Peak territory.
  - Player has proof of Orbital Command contact and a clear next directive: run the operational chain.
  - Side quest ZC-Creature-Discover-3 becomes available after this action group completes.
- Status Draft
