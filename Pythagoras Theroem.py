import math
import random


def instructions():
    """prints instructions"""

    print("""
*** Instructions ****

 To begin, choose the number of rounds (or press <enter> for
  play infinite mode).

 Then answer each question with its respective answer.

 Things you should know:
 - Entering <xxx> will stop the game and ask you if you want history or not.
 - You have to state the first two decimal places in your answer,
  do not round up or down otherwise the answer will be wrong.
  - You do not have to put the ² (Square unit) with your answer

 Good Luck !!!
    """)


# Asks the user if they want instructions (check they say yes / no)
while True:
    want_instructions = input("Do you want to see the instructions? ")

    if want_instructions in ("yes", "y"):
        instructions()
        break
    elif want_instructions in ("no", "n"):
        print("")
        break
    else:
        print("Please enter yes or no")

# Sets the round number, rounds won and the rounds lost to zero at the start of the game
round_number = 0
rounds_won = 0
rounds_lost = 0

# Asks the user if they want infinite mode or if they want to choose an amount of rounds to play
while True:
    rounds_input = input("How many rounds would you like to play? <enter> for infinite mode: ")

    if rounds_input == "":
        rounds_to_play = -1
        print("Infinite mode!")
        break
    try:
        rounds_to_play = int(rounds_input)
        print(f"Welcome to the game! {rounds_to_play} rounds!")
        break

    # Makes sure the user enters a number and nothing else
    except ValueError:
        print("Please enter a number")

# Generates random numbers to use for sides one and two (import random)
while rounds_to_play == -1 or round_number < rounds_to_play:
    side_one = random.randint(1, 5)
    side_two = random.randint(1, 5)
    a = side_one
    b = side_two

    # Generates pythagoras questions, rounds the answer to two decimal places
    c = round(math.sqrt(a ** 2 + b ** 2), 2)
    print()

    # Checks which mode the user is playing, Infinite or non Infinite
    if rounds_to_play == -1:
        print(f"Round: {round_number + 1} (Infinite Mode)")
    else:
        print(f"Round: {round_number + 1} of {rounds_to_play}")
    # Prints the two random sides and asks the question
    print(f"Side A: {side_one}, Side B: {side_two}")
    user_input = (input(f"What is Side C? "))

    # Checks if the user enters <xxx> to leave the game

    if user_input == "xxx":
        print()
        break

    # Tells the user to enter a number if they enter nothing or a letter
    if user_input == "":
        print("Enter a number")
        print("Incorrect")
        print("Please enter a number")
        round_number += 1
        rounds_lost += 1
        continue

    try:
        question = float(user_input)
    except ValueError:
        print("Enter a number")
        rounds_lost += 1
        round_number += 1
        continue

    question = float(user_input)
    # Checks if the answer is correct or incorrect
    if question == c:
        print()
        print("Correct\n")
        rounds_won += 1
        round_number += 1

    else:
        print(f"Incorrect, the answer was {c}")
        rounds_lost += 1
        round_number += 1
# Game History
game_history = f"Wins: {rounds_won}\nFails: {rounds_lost}"

if round_number > 0:
    # calculate statistics
    rounds_won = rounds_won
    percent_won = rounds_won / round_number * 100
    percent_lost = rounds_lost / round_number * 100

    # Ask user if they want to see their game history output if it requested
    while True:
        see_history = input("\nDo you want to see your Game History? ")

        if see_history in ("yes", "y"):
            print(game_history)
            print()
            break

        elif see_history in ("no", "n"):
            print("Thanks for playing")
            exit()

        else:
            print("Please enter yes or no")

    # output game statistics
    print("📊📊📊Game Statistics📊📊📊")
    print(f"👍Won: {percent_won: .2f} \t "
          f"😢Lost: {percent_lost:.2f} \t ")


