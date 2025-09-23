import sys

# entry point function
def main():
    choose = 10
    while choose:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        
        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num1 < num2:
            print(f"{num1} is less than {num2}")
        else:
            print(f"{num1} is equals to {num2}")
        
        if num1 % 2 == 0:
            print(f"{num1} is even number!!!")
        else:
            print(f"{num1} is odd number!!!")
        
        choose = int(input("Enter zero 0 to exit: "))
    
    sys.exit(0)

# Function call
main()
