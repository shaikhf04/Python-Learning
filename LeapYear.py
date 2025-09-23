import sys

def main():
    print("Leap Year Program ")
    year= int(input("Enter year: "))
    if year % 4 == 0 :
        print(f"{year} is leap year. ")
    else:
        print(f"{year} is not leap year. ")

    sys.exit()     

main()
