#  by using the pound sign you can write comments that the interpreter will ignore when the file is run. As a developer, you can use this to write notes about your code

# Variables are names givet to the data we need to store and manipulate throughout the program 
userAge = 0
# you can use the print function to display the value of a variable in the console
print(userAge)

# IMPORTANT - In python variables can only conatin letters, numbers or underscores but the first character CANNOT be a number. Camel case notation or underscores are the prefered naming conventions for variables
user_name = 'New User'
user_1 = 'User Number'
username2 = 'User number 2'

# the '=' sign is know as the assignment operator. In Python, this is how we assign a value to the right side of the = sign.
x = 5
y = 2
print(x+y)

# The basic operators are +, -, /, *, //, % and ** which rapresent addition, subtraction, division, multiplication, floor division, modulus, and exponent.

# addition 
print(x+y) # 7
# subtraction 
print(x-y) # 3
# division 
print(x/y) # 10
# multiplication 
print(x*y) # 2.5
# floor division 
print(x//y) # 2
# modulus 
print(x%y) # 1
# exponent 
print(x**y) # 25

# Unlike other programming language like Java, in python you don't need to declare a data type before storing the value. But keep in mind that you can find the data type by utilizing the type() function
print(type(1))
print(type("-2"))
print(type(False))
print(type(3.2))

# Like many other languages, Python has built in function that can help developers manipulate the data and transform it as you see fit.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# make all capitals
print(alphabet.upper())

# capitalize the first index
print(alphabet.capitalize())

# displaying many ways to formatting strings
string_name = 'Michael Jordan'
print("The name of the variable is here: {}".format(string_name))
print(f'THE NAME: {string_name}')
print("The price of this %s labtop is %d USD. I only have %.2f left."%('lenova', 2000, 2.3))

# Type casting with python
int_to_float = 18
print(float(int_to_float))
float_to_int = 17.1234
print(int(float_to_int))
# type casting a string to int and vice versa
print('{} is of type {} before casting.'.format(int_to_float, type(int_to_float)))
value_string = str(int_to_float)
print(f"{int_to_float} is of {type(value_string)} after casting.")

# Data Structures
# LIST in Python are ordered, mutable collections of heterogeneous elements. They support indexing, slicing, list comprehensions, and come with a variety of built-in methods for manipulation and iteration.
number_list = [2,5,1,6,78,10]
fruit_list = ['aaple', 'banana', 'yams','pineapples','berries']

# you can add element to the list by using append 
fruit_list.append('lemon')
print(fruit_list)
# you can display the size of a list
print(len(number_list))
# pop the last element of the list
index_pop = number_list.pop()
print(f"Once the {index_pop} was popped this is the new list: {number_list}")
# you can reverse list
fruit_list.reverse()
print(fruit_list)
# you can print the index location of a list by passing the value.
# find the index for the word pineapples and the number 1
print(number_list.index(1))
print(fruit_list.index('pineapples'))
# slice the number list right after index 4
print(number_list[:4])
# slice the new array and only print the every second element from index 0
digits = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
print(digits[0::2])
# There are planty of built in function that each of the data structure provides. To learn more visit https://docs.python.org/3/tutorial/datastructures.html
