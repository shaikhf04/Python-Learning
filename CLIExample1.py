import getopt, sys

# Entry point function
def main():
    # Local variable declarations
    argument_list = sys.argv[1:]    # removing script name
    long_options = ["help", "file", "output"] # long options
    short_options = "hfo:"  # Short hand options

    try:
        # Parsing arguments
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        # Check for the arguments
        for current_arg, current_val in arguments:
            if current_arg in ("-h", "--help"):
                print("Display Help")
            elif current_arg in ("-f", "--file"):
                print(f"file_name: {sys.argv[0]}")
            elif current_arg in ("-o", "--output"):
                print(f"output = {current_val}")
            else:
                print("Invaid command line option")
    except getopt.error as err:
        print(str(err))

    sys.exit(0)

# Function call
main()