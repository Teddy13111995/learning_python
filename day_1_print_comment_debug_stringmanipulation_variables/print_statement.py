def hello_world():
    #   print() is used to print to console.
    print("Hello World!")
    #   " " - is used for specifying strings


def string_manipulation():
    # \n is used for newline
    # + is used for concatenating two or more strings.
    # tab is used for indentation

    pass


def python_input():
    # input("A prompt for the user") - this is used to take input from user
    # # - is used for comments
    #
    name = input("What is your name?")
    print("Hello " + name)
    pass


def python_variables():
    # variables are used to store values assigned by user or program.
    # variable naming convention
    # 1. Cannot have spaces between variables
    # 2. numbers cannot be used at beginning of variables
    # 3. Do not use keywords
    # 4. NameError name is not defined
    pass

def band_name_generator():
    # Todo
    # 1. Create a greeting for your program
    print("Hello and Welcome to Band Name Generator")
    # 2. Ask the user for the city that they grew up in
    city = input("Enter the city that you grew up in\n")
    # 3. Ask the user for the name of a pet
    pet = input("Enter the name of your pet\n")
    # 4. Combine the name of their city and pet and show them their band name
    band_name = city+" "+pet
    print("Your band name could be "+band_name)
    # 5. Make sure the input cursor shows up on a new line
    pass

if __name__ == "__main__":
    # hello_world()
    # python_input()
    band_name_generator()