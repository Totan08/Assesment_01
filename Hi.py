import random

# ---------------- FUNCTIONS ----------------
def yes_no(question):
    while True:
        response = input(question).lower().strip()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer correctly")


def int_check(question, low=None, high=None, allow_exit=False, is_guess=False):
    while True:
        response = input(question).strip()

        if response == "":
            print("Please enter a number")
            continue

        if allow_exit and response.lower() == "xxx":
            return "xxx"

        if is_guess and response.lower() in ["yes", "y", "no", "n"]:
            print("Please enter a number")
            continue

        try:
            response = int(response)

            if low is not None and response < low:
                print(f"Please enter a number >= {low}")
            elif high is not None and response > high:
                print(f"Please enter a number <= {high}")
            else:
                return response

        except ValueError:
            print("Please enter a valid integer")


def instructions():
    print("""
**** Instructions ****
- Choose the number of rounds or press <enter> for infinite mode.
- Default range is 10 to 100.
- You may customise the Low and High numbers.
- Multiplication uses 'x'.
- Division uses '÷' and always produces a whole number.
- ALL answers stay inside the chosen range.
- Type 'xxx' at any time to exit the game.
""")


# ---------------- EQUATION GENERATORS ----------------
def generate_addition(low, high):
    answer = random.randint(low, high)
    num1 = random.randint(low, answer)
    num2 = answer - num1
    return num1, num2, answer, "+"


def generate_subtraction(low, high):
    answer = random.randint(low, high)
    num1 = random.randint(answer, high)
    num2 = num1 - answer
    return num1, num2, answer, "-"


def generate_multiplication(low, high):
    for _ in range(1000):
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)
        answer = num1 * num2

        if low <= answer <= high:
            return num1, num2, answer, "x"

    return generate_addition(low, high)


def generate_division(low, high):
    for _ in range(1000):
        divisor = random.randint(low, high)

        if divisor == 0:
            continue

        answer = random.randint(low, high)
        dividend = divisor * answer

        if low <= dividend <= high:
            return dividend, divisor, answer, "÷"

    return generate_addition(low, high)


# ---------------- MAIN PROGRAM ----------------
print("!!! Welcome to this Quiz game !!!\n")

if yes_no("Do you want to read the instructions? ") == "yes":
    instructions()

# ---------------- ROUNDS INPUT ----------------
while True:
    rounds_input = input("Rounds <enter for infinite>: ").strip().lower()

    if rounds_input == "":
        mode = "infinite"
        num_rounds = float("inf")
        break

    if rounds_input in ["yes", "y", "no", "n"]:
        print("You can't use that here.")
        continue

    try:
        num_rounds = int(rounds_input)
        if num_rounds <= 0:
            print("Please enter a number greater than 0.")
            continue
        mode = "regular"
        break
    except ValueError:
        print("Please enter a valid number.")

# ---------------- RANGE SETUP ----------------
use_default = yes_no("Do you want to use the default game parameters? ")

if use_default == "yes":
    low_num = 10
    high_num = 100
else:
    while True:
        low_num = int_check("Low Number? ")
        high_num = int_check("High Number? ")

        if high_num <= low_num:
            print("High number must be greater than low number.")
        else:
            break

# ---------------- GAME VARIABLES ----------------
rounds_played = 0
rounds_lost = 0
game_history = []
question_history = set()

# ---------------- GAME LOOP ----------------
while rounds_played < num_rounds:

    # ✅ UPDATED ROUND DISPLAY
    if mode == "infinite":
        print(f"\n💿 Question {rounds_played + 1} (Infinite Mode)")
    else:
        print(f"\n💿 Question {rounds_played + 1} of {int(num_rounds)}")

    # Generate unique question
    while True:
        operation = random.choice(["+", "-", "x", "÷"])

        if operation == "+":
            num1, num2, answer, op = generate_addition(low_num, high_num)
        elif operation == "-":
            num1, num2, answer, op = generate_subtraction(low_num, high_num)
        elif operation == "x":
            num1, num2, answer, op = generate_multiplication(low_num, high_num)
        else:
            num1, num2, answer, op = generate_division(low_num, high_num)

        question = f"{num1} {op} {num2}"

        if question not in question_history:
            question_history.add(question)
            break

    # Ask user
    user_answer = int_check(
        f"{question} = ",
        allow_exit=True,
        is_guess=True
    )

    if user_answer == "xxx":
        print("\nYou exited the game successfully.")
        break

    rounds_played += 1

    # Check answer
    if user_answer == answer:
        feedback = "Correct"
    else:
        feedback = f"Incorrect: The answer was {answer}"
        rounds_lost += 1

    print(feedback)

    rounds_won = rounds_played - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    game_history.append(
        f"Question {rounds_played}: {question} = {answer} | {feedback} "
        f"| 👍 {percent_won:.1f}% | 😢 {percent_lost:.1f}%"
    )

# ---------------- RESULTS ----------------
if rounds_played > 0:
    percent_won = (rounds_played - rounds_lost) / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
else:
    percent_won = percent_lost = 0

print("\n📊 Game Statistics 📊")
print(f"👍 Won: {percent_won:.2f}%")
print(f"😢 Lost: {percent_lost:.2f}%")

# ---------------- HISTORY ----------------
if yes_no("Do you want to see your game history? ") == "yes":
    if not game_history:
        print("You didn't complete any rounds, therefore we have no history but I'll give you the win anyway.")
    else:
        for item in game_history:
            print(item)

print("\nThanks for playing this Quiz!")