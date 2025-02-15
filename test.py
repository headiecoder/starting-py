def divide_it(x: float, y: float) -> float:
    return x / y


def main():
    x = float(input("Enter X:"))
    y = float(input("Enter Y:"))
    print(f"Answer is: {divide_it(x, y):.2f}")


main()
