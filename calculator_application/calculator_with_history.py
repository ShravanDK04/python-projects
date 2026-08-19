HISTORY_FILE = "history.txt"


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No history.")
            return

        print("\n--- History ---")

        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print("No history found.")


def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass

    print("History Cleared Successfully !!")


def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")


def calculate(user_input):
    input_array = user_input.split()

    if len(input_array) != 3:
        print("Invalid Input Format.")
        print("Use: NUMBER OPERATOR NUMBER")
        return

    try:
        num1 = float(input_array[0])
        num2 = float(input_array[2])
    except ValueError:
        print("Please enter valid numbers.")
        return

    operator = input_array[1]

    match operator:

        case "+":
            result = num1 + num2

        case "-":
            result = num1 - num2

        case "*":
            result = num1 * num2

        case "/":
            if num2 == 0:
                print("Cannot Divide by 0.")
                return

            result = num1 / num2

        case _:
            print("Invalid Operator.")
            return

    # Convert 5.0 to 5
    if result.is_integer():
        result = int(result)

    print("Result:", result)

    save_to_history(user_input, result)


def main():

    print("*" * 25 + " Simple Calculator " + "*" * 25)

    while True:

        user_input = input(
            "\nEnter expression or command (history, clear, exit): "
        ).strip()

        match user_input.lower():

            case "exit":
                print("Thank you for using the calculator!")
                break

            case "history":
                show_history()

            case "clear":
                clear_history()

            case _:
                calculate(user_input)


main()