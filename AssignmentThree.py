 # 2026 FIFA WORLD CUP MANAGER SIMULATION
# Concepts used: for loop, while loop, break, continue, pass

import random

# Team stats
team_name = "Your Nation FC"
morale = 70
strength = 70
injuries = 0
wins = 0
losses = 0
draws = 0
eliminated = False
champion = False


def show_stats():
    print("\n     Team Stats    ")
    print("Team:", team_name)
    print("Morale:", morale)
    print("Strength:", strength)
    print("Injuries:", injuries)
    print("Record: W" + str(wins) + " D" + str(draws) + " L" + str(losses))
    print("\n")


def clamp(value):
    # Keep stats between 0 and 100
    if value < 0:
        return 0
    elif value > 100:
        return 100
    else:
        return value


def match_result(opp_strength):
    # Calculate match outcome based on team stats
    penalty = injuries * 3
    bonus = (morale - 50) // 5
    my_power = strength + bonus - penalty + random.randint(-15, 15)
    opp_power = opp_strength + random.randint(-15, 15)

    print("Your power:", my_power, "| Opponent power:", opp_power)

    if my_power > opp_power + 5:
        return "win"
    elif my_power < opp_power - 5:
        return "loss"
    else:
        return "draw"

# PRE-TOURNAMENT PREPARATION
# Uses: for loop, continue, pass

print("PHASE 1: PRE-TOURNAMENT PREPARATION")


sessions = ["Session 1", "Session 2", "Session 3"]

for session in sessions:
    # for loop - goes through each session   
    print("\n--", session, "--")
    show_stats()

    # If team is already very strong, skip training (continue)
    if strength >= 95 and morale >= 95:
        print("Team is at peak! Skipping this session.")
        # CONTINUE - skip to next session
        continue   

    print("Choose an activity:")
    print("1 - Intense Training  (strength +8, risk of injury)")
    print("2 - Friendly Match    (morale +10, strength +3)")
    print("3 - Rest & Recovery   (heal injuries, morale +8)")
    print("4 - Tactical Study    (strength +5)")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        strength = clamp(strength + 8)
        if random.random() < 0.35:
            injuries += 1
            print("Great training! But a player got injured.")
        else:
            print("Training went well! Strength increased.")

    elif choice == "2":
        morale = clamp(morale + 10)
        strength = clamp(strength + 3)
        print("Friendly match done! Morale and strength up.")

    elif choice == "3":
        if injuries > 0:
            injuries -= 1
            print("One player recovered from injury.")
        morale = clamp(morale + 8)
        print("Rest day complete. Morale up.")

    elif choice == "4":
        strength = clamp(strength + 5)
        print("Tactical study done. Strength up.")

    else:
        print("Invalid choice. Nothing happened.")

    # Placeholder for future press conference feature
     # PASS does nothing, just a placeholder
    pass  
print("\nPreparation phase done!")
show_stats()

# GROUP STAGE (3 matches)
# Uses: for loop, continue, break

print("PHASE 2: GROUP STAGE")

group_opponents = [
    ["Brazil", 82],
    ["Germany", 78],
    ["Senegal", 72]
]

points = 0

for i in range(len(group_opponents)):   # for loop - 3 group matches
    opponent_name = group_opponents[i][0]
    opponent_strength = group_opponents[i][1]

    print("\nMatch", i + 1, "vs", opponent_name)
    show_stats()

    # If already eliminated early, stop playing (break)
    if losses >= 2 and points == 0:
        print("Team is mathematically eliminated. No point playing on.")
        eliminated = True
        break   # BREAK - exit the group stage loop

    print("Choose your strategy:")
    print("a - Attack  (strength +2 for this match)")
    print("b - Balanced (no changes)")
    print("c - Defend  (strength -2 for this match)")

    strategy = input("Enter a, b, or c: ")

    if strategy == "a":
        strength = clamp(strength + 2)
    elif strategy == "c":
        strength = clamp(strength - 2)

    result = match_result(opponent_strength)

    # Revert strategy change after match
    if strategy == "a":
        strength = clamp(strength - 2)
    elif strategy == "c":
        strength = clamp(strength + 2)

    if result == "win":
        points += 3
        wins += 1
        morale = clamp(morale + 10)
        print("RESULT: WIN! Great performance!")

    elif result == "draw":
        points += 1
        draws += 1
        print("RESULT: DRAW. Not bad.")

    else:
        points += 0
        losses += 1
        morale = clamp(morale - 8)
        print("RESULT: LOSS. Tough day.")

    # Small injury chance each match
    if random.random() < 0.2:
        injuries += 1
        print("A player got injured during the match.")

    # Skip press conference if morale is very low
    if morale < 40:
        print("Morale too low for press conference. Skipping it.")
        # CONTINUE - skip rest of this loop iteration
        continue   
    print("Press conference held after the match.")

print("\nGroup stage done! Total points:", points)

if points < 4:
    print("Not enough points. Your team is ELIMINATED.")
    eliminated = True
else:
    print("QUALIFIED for the knockout stage!")

show_stats()

#KNOCKOUT STAGE
# Uses: while loop, break, pass

print("=" * 40)
print("PHASE 3: KNOCKOUT STAGE")
print("=" * 40)

knockout_rounds = [
    ["Round of 16",   "Argentina", 83],
    ["Quarter-Final", "France",    85],
    ["Semi-Final",    "England",   80],
    ["The Final",     "Spain",     87]
]

round_index = 0

while round_index < len(knockout_rounds):
    # while loop - keeps going until out or champion  
    if eliminated:
        break  
     # BREAK - team already eliminated, stop the loop

    round_name     = knockout_rounds[round_index][0]
    opponent_name  = knockout_rounds[round_index][1]
    opp_strength   = knockout_rounds[round_index][2]

    print("\n***", round_name, "***")
    print("Opponent:", opponent_name)
    show_stats()

    print("Choose preparation:")
    print("1 - Extra Training  (strength +4)")
    print("2 - Team Talk       (morale +8)")
    print("3 - Full Rest       (heal 1 injury, morale +4)")

    prep = input("Enter 1, 2, or 3: ")

    if prep == "1":
        strength = clamp(strength + 4)
        print("Training done. Strength up!")

    elif prep == "2":
        morale = clamp(morale + 8)
        print("Team talk done. Morale up!")

    elif prep == "3":
        if injuries > 0:
            injuries -= 1
        morale = clamp(morale + 4)
        print("Rest complete. Feeling fresh!")

    else:
        print("Invalid choice. No prep done.")

    result = match_result(opp_strength)

    if result == "win":
        wins += 1
        morale = clamp(morale + 12)
        print("RESULT: WIN! You advance to the next round!")

        if round_name == "The Final":
            champion = True
            break  
         # BREAK if won the World Cup, no more matches

        round_index += 1   # move to next round

    elif result == "draw":
        print("DRAW after 90 minutes! Going to penalties...")
        if random.random() > 0.45:
            wins += 1
            morale = clamp(morale + 8)
            print("You win on PENALTIES! Advancing!")

            if round_name == "The Final":
                champion = True
                break   
            # BREAK coz won the World Cup on penalties

            round_index += 1

        else:
            losses += 1
            morale = clamp(morale - 10)
            eliminated = True
            print("Lost on penalties. You are ELIMINATED.")
            break   
        # BREAK ( out of the tournament)

    else:
        losses += 1
        morale = clamp(morale - 12)
        eliminated = True
        print("RESULT: LOSS. You are ELIMINATED.")
        break  
     # BREAK (out of the tournament)
    # Placeholder for future transfer window feature between rounds
    pass  
 # PASS (placeholder, nothing here yet)
# FINAL RESULT

print("\n" + "=" * 40)
if champion:
    print("CONGRATULATIONS! YOU ARE WORLD CUP CHAMPIONS!")
else:
    print("Tournament over. Better luck next time.")

print("Final record: W" + str(wins) + " D" + str(draws) + " L" + str(losses))
show_stats()