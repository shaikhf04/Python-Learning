# Import libraries
import sys
import re
import math

# Entry point function
def main():
    mystr = "India is my country. All Indians are my brothers and sisters. Except 1"

    findstr = re.search("my", mystr)

    print(f"Find String: {findstr}")
    if type(findstr) == re.Match:
        print(f"Type: {type(findstr)} String Position: {findstr.start()} to {findstr.end()} \
              Group: {findstr.group()} Span: {findstr.span()}")
    else:
        print(f"Type: {type(findstr)} String not found")
    
    findstr = re.findall("my", mystr)
    print(f"Find All String: {findstr}")   

    findstr = re.split("\n", mystr) 
    print(f"Split String: {findstr}")

    findstr = re.search("c..nt", mystr)
    print(f"Find String: {findstr}")

    findstr = re.search("[0-9]", mystr)
    print(f"Find String: {findstr}")

    findstr = re.search("^All.*$", mystr)
    print(f"Find String: {findstr}")


    print("###Math Library Usage###")
    val = -25
    print(f"Absolute value of {val} is {abs(val)}")

    to_power = 3
    val = 2
    print(f"{val} to the power {to_power} is {math.pow(val, to_power)} func: {val ** to_power}")

    val = 16
    print(f"Square root of {val} is {math.sqrt(val)}")

    print(f"Value of cosine is {math.cos(0)}")
    
    sys.exit(0)

# Function call
main()