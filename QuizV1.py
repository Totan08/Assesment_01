import random


# -------------------- Helper Functions --------------------
def yes_no(question):
    while True:
        response = input(question).lower().strip()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        print("Please answer correctly")


def int_check(question, allow_exit=False):
    while True:
        response = input(question).strip()
        if allow_exit and response.lower() == "xxx":
            return "xxx"
        try:
            return int(response)
        except ValueError:
            print("Please enter a valid integer or 'xxx' to exit.")


def instructions():
    print("""
                **** Instructions ****
                
- Choose number of rounds or press <enter> for infinite mode.
- Choose operations (+, -, x, ÷) first.
- Then choose difficulty (Easy / Medium / Hard) which automatically sets the range.
- Multiplication appears more often.
- Division always produces a whole number.
- Type 'xxx' at any time to exit.
- Use "/" for Division (÷)

            🍀🍀🍀 Good Luck! 🍀🍀🍀
""")


# -------------------- Operation Selection --------------------
def choose_operations():
    valid_ops = ["+", "-", "x", "/"]
    while True:
        choice = input("Choose operations (+ - x ÷): ").lower().split()
        selected = [op for op in choice if op in valid_ops]
        if selected:
            return selected
        print("Choose at least one valid operation.")


# -------------------- Difficulty Selection --------------------
def choose_difficulty():
    while True:
        choice = input("Easy, Medium or Hard mode? ").lower().strip()
        if choice in ["easy", "e"]:
            return 1, 12, "Easy"
        elif choice in ["medium", "m"]:
            return 13, 40, "Medium"
        elif choice in ["hard", "h"]:
            return 50, 100, "Hard"
        else:
            print("Please choose Easy, Medium or Hard.")


# -------------------- Weighted Shuffle --------------------
def weighted_shuffle(questions):
    weighted = []
    for q in questions:
        weighted.extend([q] * 3 if q[3] == "x" else [q])
    random.shuffle(weighted)
    return weighted


# -------------------- Question Pool --------------------
def generate_question_pool(low, high, ops):
    pool = []
    seen = set()

    def make_key(a, b, op):
        if op in ["+", "x"]:
            return (min(a, b), max(a, b), op)
        return (a, b, op)

    # Addition
    if "+" in ops:
        for a in range(low, high + 1):
            for b in range(low, high + 1):
                key = make_key(a, b, "+")
                if key not in seen:
                    seen.add(key)
                    pool.append((a, b, a + b, "+"))

    # Subtraction
    if "-" in ops:
        for a in range(low, high + 1):
            for b in range(low, a + 1):
                key = make_key(a, b, "-")
                if key not in seen:
                    seen.add(key)
                    pool.append((a, b, a - b, "-"))

    # Multiplication
    if "x" in ops:
        for a in range(low, high + 1):
            for b in range(low, high + 1):
                answer = a * b
                key = make_key(a, b, "x")
                if key not in seen:
                    seen.add(key)
                    pool.append((a, b, answer, "x"))

    # Division
    if "/" in ops:
        for divisor in range(low, high + 1):
            for answer in range(low, high + 1):
                dividend = divisor * answer
                key = make_key(dividend, divisor, "÷")
                if key not in seen:
                    seen.add(key)
                    pool.append((dividend, divisor, answer, "÷"))

    return pool


# -------------------- Main Program --------------------
print("!!! Welcome to this Quiz game !!!\n")
if yes_no("Do you want to read the instructions? ") == "yes":
    instructions()

# -------------------- Rounds --------------------
while True:
    rounds_input = input("Rounds <enter for infinite>: ").strip()
    if rounds_input == "":
        mode = "infinite"
        num_rounds = float("inf")
        break
    try:
        num_rounds = int(rounds_input)
        if num_rounds > 0:
            mode = "regular"
            break
        print("Enter number >0")
    except:
        print("Invalid input")

# -------------------- Operations --------------------
selected_ops = choose_operations()

# -------------------- Difficulty --------------------
low_num, high_num, difficulty_name = choose_difficulty()


# -------------------- Generate Questions --------------------
question_pool = generate_question_pool(low_num, high_num, selected_ops)
if not question_pool:
    print("No valid questions possible.")
    exit()
question_pool = weighted_shuffle(question_pool)

# -------------------- Game Variables --------------------
rounds_played = 0
rounds_lost = 0
game_history = []
index = 0

# -------------------- Game Loop --------------------
while rounds_played < num_rounds and index < len(question_pool):
    if mode == "infinite":
        print(f"\n💿 Question {rounds_played + 1} (Infinite Mode, Current Mode: {difficulty_name})")


    else:
        print(f"\n💿 Question {rounds_played + 1} of {int(num_rounds)} | Current Mode: {difficulty_name} 💿")

    num1, num2, answer, op = question_pool[index]
    index += 1
    print(f"Answer: {answer}")
    user = int_check(f"{num1} {op} {num2} = ", allow_exit=True)
    if user == "xxx":
        break

    rounds_played += 1
    if user == answer:
        feedback = "Correct!"
    else:
        feedback = f"Incorrect: The answer was {answer}"
        rounds_lost += 1
    print(feedback)


    won = rounds_played - rounds_lost
    percent_won = won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    game_history.append(

        f"Question {rounds_played}: {num1} {op} {num2} = {answer} | {feedback} | {percent_won:.1f}% | {percent_lost:.1f}% | ")

# -------------------- Results --------------------
if rounds_played > 0:
    percent_won = (rounds_played - rounds_lost) / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
else:
    percent_won = percent_lost = 0

print("\n📊 Game Statistics 📊")
print(f"👍 Won: {percent_won:.2f}%")
print(f"😢 Lost: {percent_lost:.2f}%")
print()

# -------------------- History --------------------
if yes_no("See game history? ") == "yes":
    print()
    for item in game_history:
        print(item)
    else:
        if rounds_played == 0:
            print("You didn't play any rounds, therefore there is no history to show")

print("\n!!! Thanks for playing !!!")
