# basic data types in python are strings, integer, float and boolean

#strings
str_1 = "Hello"[0]  #subscripting
print(str_1)

str_1 = "Hello"[4]
print(str_1)

# number inside the quotes is treated as string.


# Integer - number without any decimal places

print(123+345)

# putting underscore between numbers is used commas in larger integer
print(123_456_789)

# float - numbers with decimal point

# boolean - True/ False

# type() is used to find data type of variable
##num_char = len(input("Enter your name?"))

##print("your name has "+ num_char+" letters.")

# A TypeError is generated as num_char has type int
# to resolve this issue we type cast num_char to string by using str()

num_char = str(len(input("Enter your name?")))

print("your name has "+ num_char+" letters.")

# you can type cast any data type to any data type by using int(),float(),str().
a = 123
print(type(a))
print(type(str(a)))
print(type(float(a)))