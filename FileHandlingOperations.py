import sys
import os

# Global function definitions
def readFile(file_name):    # Function definition
    # Exception handling
    try:
        with open(file_name, "r") as file_handle:
            print("Contents of the file:\n" + file_handle.read())
    except FileNotFoundError:
        print(f"File not found: {file_name}")

def writeFile(file_name):   # Function definition
    file_handle = open(file_name, "w")
    if file_handle:
        contents = input("Enter the contents to write to the file: ")
        file_handle.write(contents)            
        file_handle.close()
    else:
        print("File not found: {file_name}")

def appendFile(file_name):  # Function definition
    file_handle = open(file_name, "a")
    if file_handle:
        contents = input("Enter the contents to append to the file: ")
        file_handle.write(contents)
        file_handle.close()
    else:
        print("File not found: {file_name}")

def deleteFile(file_name):  # Function definition
    # Exception handling
    try:
        os.remove(file_name)
        print(f"File deleted: {file_name}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")

# Entry point function
def main():
    file_name = input("Enter the file name: ")

    while file_name:
        file_operation = input("Enter the file operation: (r for read, w for write, a for append, d for delete, e to exit loop): ")

        if file_operation == "r":
            readFile(file_name)     # Function call
        elif file_operation == "w":
            writeFile(file_name)    # Function call
        elif file_operation == "a":
            appendFile(file_name)   # Function call
        elif file_operation == "d":
            deleteFile(file_name)   # Function call
        elif file_operation == "e":
            break
        else:
            print("Invalid file operation")
    
    sys.exit(0)

# Function call
main()