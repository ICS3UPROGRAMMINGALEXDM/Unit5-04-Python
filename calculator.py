#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: gets an operation and two numbers from user, calulates an answer
# with the numbers and operation entered

# function checks which opertaion was entered then calculates the results with
# the inputted parameters
def calculate(operation, num1flt, num2flt):
    # checks which operation was entered
    if operation == "/":
        result = num1flt / num2flt
    elif (operation == "*") or (operation == "x"):
        result = num1flt * num2flt
    elif operation == "+":
        result = num1flt + num2flt
    elif operation == "-":
        result = num1flt - num2flt
    else:
        result = "The inputted operation was invalid"

    # sends this back to main
    return result


def main():
    # getting user input
    operation = input("Enter the operation of your equation: ").strip()
    num1 = input("Enter the first number to be calculated: ").strip()
    num2 = input("Enter the second number to be calculated: ").strip()

    try:
        # converting to float
        num1flt = float(num1)
        num2flt = float(num2)
        # calling the calculate function
        answer = calculate(operation, num1flt, num2flt)
        # outputting results
        if answer == "The inputted operation was invalid":
            print(answer)
        else:
            print("\n{1} {2} {3} = {0}".format(answer, num1, operation, num2))
    except ValueError:
        print("Numbers entered must be actual numbers")


if __name__ == "__main__":
    main()
