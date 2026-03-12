import math
import random


def yes_no(question):
    """Checks user response to a questin is yes / no (y/), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / Y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """prints instructions"""

    print("""
**** Instructions ****

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the 
number of rounds will be 15).

If you would like you can enter infinite mode. Press Enter
to go into infinite mode.

Your goal is to try to answer as manny questions as you can! 

Good Luck ! 
    """)


# check for an integer with optional upper /
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is not None:
        error = (f"Please enter an integer that is "
                 f"more than {low} / equal {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that "
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit mode
        if exit_code is not None and response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response


        except ValueError:
            print(error)


def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response in a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Inialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""
rounds_lost = 0

game_history = []
all_scores = []

print("!!! Welcome To This Quiz Game !!!")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# check user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose low / high number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# calc
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts
while rounds_played < num_rounds:

    # rounds heading
    if mode == "infinite":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} (Infinite Mode) 💿💿💿"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    # round starts here
    # set guesses to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # choose a "secret" number between the low and high number
    secret = random.randint(low_num, high_num)
    # print("Spoiler Alert!!!", secret)       # remove this line after testing !!!

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number...
        guess = int_check(f"Question 1: ", low_num, high_num, "xxx")

        if guess == "xxx":
            end_game = "yes"
            break

            # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}.  You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

            # if guess is not a duplicate, add it to the "already guessed" list
        else:
            already_guessed.append(guess)

        # add one to the number of guesses used
        guesses_used += 1

        # compare the user's guess with the secret number set up feedback statement

        # if we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number"
                        f" You've used {guesses_used} / {guesses_allowed} guesses ")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number"
                        f" You've used {guesses_used} / {guesses_allowed} guesses ")

        # when the secret number is guessed, we have three different feedback
        # options (lucky / phew / well done)
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! you got is on the first guess. 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses. "
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} Guesses!"
        # if there are no guesses left!
        else:
            feedback = f'Sorry you have no more guesses. You lose this round! The super secret number was: {secret}!'
            rounds_lost += 1

        # print feedback to user
        print(feedback)

        # Additional feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            careful = ("\n💣💣💣 Careful you have one guess left! 💣💣💣\n")
            if guess == secret:
                feedback = f"Phew! You got it in {guesses_used} guesses. "
            else:
                print(careful)

    # round ends here

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break

    rounds_played += 1

    # add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"
    print(history_feedback)
    game_history.append(history_feedback)

if rounds_played > 0:
    # calculate statistics
    rounds_won = rounds_played - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # output game statistics
    print()
    print("📊📊📊Game Statistics📊📊📊")
    print(f"👍Won: {percent_won: .2f} \t "
          f"😢Lost: {percent_lost:.2f} \t ")

    # Ask user if they want to see their game history output if it requested
    see_history = string_checker("\nDo you want to see your Game History? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing !")
