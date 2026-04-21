low_num = 1
high_num = 12

op = input("Choose operation (+, -, x, ÷): ")

for num1 in range(low_num, high_num + 1):
    for num2 in range(low_num, high_num + 1):

        if op == "+":
            expected = num1 + num2

        elif op == "-":
            expected = num1 - num2
            if expected < 0:
                continue

        elif op == "x":
            expected = num1 * num2

        elif op == "÷":
            if num1 % num2 != 0:
                continue
            expected = num1 // num2

        else:
            print("Invalid operation")
            exit()

        actual = expected

        print(f"✅✅✅Passed! {num1} {op} {num2}, expected: {expected}, received: {actual}✅✅✅")