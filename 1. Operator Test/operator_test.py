import operators

def main():
    start = input("Press only ENTER to start: ")

    while start == "":

        x = int(input("\nInput first number: "))
        y = int(input("Input second number: "))

        print(f"\n{x} plus {y} = {operators.add(x, y)}")
        print(f"{x} minus {y} = {operators.subtract(x, y)}")
        print(f"{x} multiplied by {y} = {operators.multiply(x, y)}")

        try:
            print(f"{x} divided by {y} = {operators.divide(x, y):.2f}\n")
        except ZeroDivisionError:
            print(f"{x} divided by {y} is undefined.\n")

        start = input("Press ENTER to restart: ")

    print("\nGoodbye!")


if __name__ == "main":
    main()
    