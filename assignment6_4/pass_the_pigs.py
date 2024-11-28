# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Nea Rantanen
# Template for Exercise 6.4

import random

WIN = 60
SINGLE_PIG = ["Side (no dot)", "Side (dot)", "Razorback", "Trotter", "Snouter", "Leaning Jowler"]
PROBS = [0.35, 0.65, 0.87, 0.96, 0.99, 1]
SINGLE_PIG_POINTS = {"Side (no dot)": 0, "Side (dot)": 0, "Razorback": 5, "Trotter": 5, "Snouter": 10,
                     "Leaning Jowler": 15}
BOTH_PIGS = {"Side (no dot)": "Sider", "Side (dot)": "Sider", "Razorback": "Double Razorback",
             "Trotter": "Double Trotter", "Snouter": "Double Snouter", "Leaning Jowler": "Double Leaning Jowler"}
BOTH_PIGS_POINTS = {"Sider": 1, "Double Razorback": 20, "Double Trotter": 20, "Double Snouter": 40,
                    "Double Leaning Jowler": 60}


def throw_pig():
    luku = random.random()
    i = 0
    while PROBS[i] <= luku:
        i += 1
    return SINGLE_PIG[i]

    #The function returns the outcome (string) of tossing one pig.


def throw_two_pigs():
    pig_one = throw_pig()
    pig_two = throw_pig()

    if pig_one == pig_two:
        name = BOTH_PIGS[pig_one]
        points = BOTH_PIGS_POINTS[name]

    elif pig_one == SINGLE_PIG[0] and pig_two == SINGLE_PIG[1] \
            or pig_one == SINGLE_PIG[1] and pig_two == SINGLE_PIG[0]:
        name = "Pig out"
        points = 0

    else:
        name = "Other combo: {} + {}".format(pig_one, pig_two)
        points = SINGLE_PIG_POINTS[pig_one] + SINGLE_PIG_POINTS[pig_two]
        
    return name, points

    #The function throws two pigs and returns the name (string) and points (int) of the combo.


def main():
    print("Play a game of pass the pigs against the computer!")
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    print()
    player_points = 0
    computer_points = 0
    game = True

    while game:
        print("------------------------------")
        print("It's your turn to pass the pigs!")
        round = True
        i = 1
        points_in_round = 0
        while round:
            name, points = throw_two_pigs()
            print("{}. {}, {} points".format(i, name, points))
            if name == "Pig out":
                print("The turn ended. Points from this turn were set to 0.")
                round = False
            else:
                points_in_round += points
                print("{} points gathered this round!".format(points_in_round))
                if player_points + points_in_round >= WIN:
                    player_points += points_in_round
                    print("The total score of {} (>= 60) points reached! The turn ends.".format(player_points))
                    round = False
                else:
                    print('Enter "yes" if you want to continue your turn.')
                    rivi = input()
                    if rivi != "yes":
                        player_points += points_in_round
                        round = False
                    i += 1

        input("Press enter to continue.")
        print()
        print("------------------------------")
        print("It's computer's turn to pass the pigs!")
        round = True
        i = 1
        points_in_round = 0

        while round:
            name, points = throw_two_pigs()
            print("{}. {}, {} points".format(i, name, points))
            if name == "Pig out":
                print("The turn ended. Points from this turn were set to 0.")
                round = False
            else:
                points_in_round += points
                print("{} points gathered this round!".format(points_in_round))
                if player_points < 60:
                    if points_in_round >= 10 or (computer_points + points_in_round) >= WIN:
                        computer_points += points_in_round
                        if computer_points >= WIN:
                            print("The total score of {} (>= 60) points reached! The turn ends." \
                                  .format(computer_points))
                        round = False
                else:
                    if (computer_points + points_in_round) > player_points:
                        computer_points += points_in_round
                        print("The total score of {} (>= {}) points reached! The turn ends." \
                              .format(computer_points, player_points + 1))
                        round = False
                i += 1

        input("Press enter to continue.")
        print()
        print("------------------------------")
        print("Your score: {}".format(player_points))
        print("Computer's score: {}".format(computer_points))
        
        if player_points >= WIN or computer_points >= WIN:
            if player_points != computer_points:
                print()
                if player_points > computer_points:
                    print("You won! Congratulations!")
                else:
                    print("Computer won!")
                game = False

main()
