import sys

def main():
    print("Table Program ")
    number= int(input("Enter number to print table: "))
    i=1
    while i <= 10 :
        table = number * i
        print(f"{number} * {i} =\t {table}")
        i = i+1
    sys.exit()     

main()
