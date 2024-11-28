# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Anni Niskanen
# Template for Exercise 9.2


from golfer import Golfer
from golf_course import GolfCourse


def ask_list_of_integers():
    """
    Asks the user for integers separated by commas. Converts the inputted string into a list of integers and
    returns it.
    """
    string = input()
    list_in_characters = string.split(",")  # creates a list
    list_in_integers = []
    for character in list_in_characters:
        list_in_integers.append(int(character))
    return list_in_integers


def main():
    input("Press enter to continue.\n")

    # Create two golfers and one golf course here
    golfer1_name = input("Name of the first golfer:\n")
    golfer1 = Golfer(golfer1_name)
    golfer2_name = input("Name of the second golfer:\n")
    golfer2 = Golfer(golfer2_name)

    golf_course = input("Name of the golf course:\n")
    print("Par scores of the golf course (separated by commas):")
    scores = ask_list_of_integers()
    slope_rating = int(input("Slope rating of the golf course:\n"))
    input()

    # Print information about the golfers and the golf course here
    print("The golfers:")
    print("{}: handicap {}".format(golfer1.get_name(), golfer1.get_handicap()))
    print("{}: handicap {}".format(golfer2.get_name(), golfer2.get_handicap()))
    print()
    print("The golf course:")
    golf_info = GolfCourse(golf_course, scores, slope_rating)
    print(golf_info)
    input()
    
    # The golfers play a round of Golf here
    print("{} and {} are off to play a round of Golf in {}!"
          .format(golfer1.get_name(), golfer2.get_name(), golf_info.get_name()))
    print("Enter {}'s results (separated by commas):".format(golfer1.get_name()))
    golfer1_results = ask_list_of_integers()
    print("Enter {}'s results (separated by commas):".format(golfer2.get_name()))
    golfer2_results = ask_list_of_integers()
    input()

    # Print the results of the first golfer here
    print("{}'s round looks like this:".format(golfer1.get_name()))
    statistic1 = golfer1.get_round_statistics(golf_info, golfer1_results)
    print(statistic1)
    input()

    # Print the results of the second golfer here
    print("And {}'s round looks like this:".format(golfer2.get_name()))
    statistic2 = golfer2.get_round_statistics(golf_info, golfer2_results)
    print(statistic2)
    input()

    # Determine and print which golfer won the game here
    results = golfer1.compare_scores(golfer1_results, golfer2_results)
    if results == True:
        print("{} won the round!".format(golfer1.get_name()))
    else:
        print("{} won the round!".format(golfer2.get_name()))
    input()

    # Print how much the golfers' handicaps lowered here
    print("The golfers have played {} holes in {} and count their new handicaps."
          .format(golf_info.get_amount_of_holes(), golf_info.get_name()))

    golfer1_handicap = golfer1.play_round(golf_info, golfer1_results) #tasoitus ensimmäisen kierroksen jälkeen
    golfer2_handicap = golfer2.play_round(golf_info, golfer2_results)
    print("{}'s handicap lowered by {}.".format(golfer1.get_name(), golfer1_handicap))
    print("{}'s handicap lowered by {}.".format(golfer2.get_name(), golfer2_handicap))
    input()

    # Print information about the golfers again here
    print("The golfers again:")
    print("{}: handicap {}".format(golfer1.get_name(), golfer1.get_handicap()))
    print("{}: handicap {}".format(golfer2.get_name(), golfer2.get_handicap()))
    input()

    # Compare the golfers with each other and print which one has a lower handicap
    lower_handicap = golfer1.compare_golfers(golfer2)
    if lower_handicap == True:
        print("{} has a lower handicap.".format(golfer1.get_name()))
    else:
        print("{} has a lower handicap.".format(golfer2.get_name()))

main()