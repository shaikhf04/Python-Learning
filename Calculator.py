"""
    Simple calculator program.
"""
import sys

# Entry point function
def main():
    choose = 100
    while choose:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        print("Choose the operations from the following choices: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Reminder")
        print("0. Exit")

        choose = int(input("Enter the option: "))

        if 1 == choose:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif 2 == choose:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif 3 == choose:
            result = num1 * num2
            print(f"{num1} x {num2} = {result}")
        elif 4 == choose:
            if 0 == num2:
                print("[ERROR] denominator must be greater than zero.\nPlease retry with non-zero denominator")
                continue                
            
            result = num1 / num2
            print(f"{num1} /{num2} = {result}")
        elif 5 == choose:
            print(f"{num1} % {num2} = {num1 % num2}")
        elif 0 == choose:
            break
        else:
            print("Wrong option selected.\nPlease try again...")
    
    sys.exit(0)

# Function call
main()
