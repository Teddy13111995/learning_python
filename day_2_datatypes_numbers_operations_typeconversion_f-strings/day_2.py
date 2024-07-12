def datatypes_python():
    """
    Basic data types
    1.  String
    2.  Integer
    3.  Float
    4.  Boolean


    :return:
    """
    print("Hello"[-1])
    print("123" + "456")

    # _ is used with nos to show ,
    print(123_456_789)
    pass


def typeerror_python():
    """
    type() - identifies the variable's data type.
    type casting - converting one data type to another.

    :return:
    """
    pass


def mathematical_operations():
    """
    + - add
    - - subtract
    * - multiply
    / - divide with floating point
    //- floor division
    ** - exponent
    priority -> PEMDASLR(Parentheses, Exponents, Multiplication, Division, Addition, Subtraction, Left, Right)
    """
    pass


def number_manipulation():
    """
    round(number, no. of decimal places) - round the number to number of digits.
    // - floor division
    +=,-=,*=,/= - shorthand
    f-string -> f'{variable1} is integer'

    """
    pass


def tip_calculator():
    # If the bill was $150.00, split between 5 people, with 12% tip.

    # Each person should pay (150.00 / 5) * 1.12 = 33.6
    # Format the result to 2 decimal places = 33.60

    # Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

    # Write your code below this line 👇
    print("Welcome to tip calculator!")
    total_bill = float(input("What was the total bill?"))
    tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?"))
    num_of_person = int(input("How many people to split the bill?"))
    split = round(total_bill*(1+tip_percent*0.01)/7,2)
    print(f"Each person should pay: {split}")
    pass


if __name__ == "__main__":
    # datatypes_python()
    tip_calculator()