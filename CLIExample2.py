# Libraries
import sys

# Global function definition
def sumOfIntegers(integer_vector):
    sum = 0
    for x in integer_vector:
        sum = sum + int(x)
    return sum

# Entry point function
def main():
    number_of_arguments = len(sys.argv)
    print(f"Number of arguments: {number_of_arguments}")
    print(f"Name of python program: {sys.argv[0]}")
    print("Arguments passed:")
    for cmd in range(1, number_of_arguments):
        print(f"{sys.argv[cmd]}")

    print(f"Sum of integers = {sumOfIntegers(sys.argv[1:])}")
    
    sys.exit(0)

# Function call
main()