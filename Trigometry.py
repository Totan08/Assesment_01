import random
import string
# checks the user enters yes or no
def yes_no(question):
    while True:
        response = input(question).lower().strip()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
print("Trigonometry Quiz !!!\n")
# instructions (if wanted)
def instructions():
    print("""
        You will be given two sides of a Triangle, (A), (O) or (H) and you will have to state the missing side!
                                        Type <xxx> to quit the game at any point!
                                                   Good luck! 🍀🍀🍀
    """)
if yes_no("Do you want the instructions? ") == "yes":
    instructions()

def history_want():
    print(f"You got {rounds_won} / {num_rounds} Correct!")
    print(f"You got {rounds_lost} / {num_rounds} Correct!")
# Allows the user to choose the amount of rounds they want to play
print()
num_rounds = int(input("To play a lot of rounds, enter a large number. How many rounds do you want to play? "))

print(f"You picked to play {num_rounds} rounds")
rounds_won = 0
rounds_lost = 0
print()
wrong_answer_check = random.choice(string.ascii_letters)
round = 1
history = ""

# Picks a random side from the choice and makes it the missing side, then prints the question (loops)

while True:
    missing_side = random.choice(["A", "H", "O"])
    print(f"Round: {round} of {num_rounds}\n")

    if missing_side == "A":
        print("O")
        print("H\n")

    if missing_side == "O":
        print("A")
        print("H\n")

    if missing_side == "H":
        print("O")
        print("A\n")

    answer = input("Which side is missing? ")

    if answer == "xxx":
        history = input("Do you want your game history? ")
        if history == "no" or "n":
            break

        if history == "yes" or "y":
            print(f"You won {rounds_won} out of {num_rounds} Rounds!")
            print(f"You lost {rounds_lost} out of {num_rounds} Rounds!")
            break

    if answer == missing_side:
        print("Yes\n")
        round += 1
        rounds_won += 1
    else:
        print(f"No, it was ({missing_side})")
        round += 1
        rounds_lost += 1

    if round == num_rounds + 1:
        print(f"You've played all {num_rounds} Rounds ! ")
        print()

# Game history area

    history = (f" You won {rounds_won} / {num_rounds}!")
    if round == num_rounds + 1:
        if yes_no("Do you want your history? ") == "yes":
            history_want()
            break
        else:
            "Thanks for playing !!!"
            break















