# Function, Modules
# Functions and methods in Python are blocks of reusable code that perform specific tasks. Functions are blocks of code that take zero or more arguments as input, perform some operations, and optionally return a result while Methods are functions that are associated with objects and are called using dot notation (object.method()). 
# EXAMPLE OF A METHOD IN ACTION
string_value = 'You don\'t know my name.'
# use the upper method to turn all the letter capitale
string_value = string_value.upper()
print(string_value+' \n')
# create your own fuction that when calls will print Hello World
def hello_world():
    print('This is the hello_world() function. Hello World\n')
      
hello_world()

# create a function that return the value.
def return_function():
    return """This function return a string. 
In order to see the return you have to use the print() method"""

print(return_function())

# create a function and pass parameter to get the exponent of the first parameter. use return.
def exponent(x, y):
    return x**y

print(exponent(6,2)) # 36

# VARIABLE LOCAL & GLOBAL SCOPE
# Local Scope: Variables defined within a function are said to have a local scope. They can only be accessed from within that function. Once the function completes execution, the local variables are destroyed, and their memory space is freed.

# global scope example
message = 'I AM A GLOBAL SCOPE'

def my_function():
    """This function will display the global scope"""
    return message
print(my_function())


# try to change the global scope and see what happens when you print the message veriable after the change_function is being called
def change_function(word):
    message = word
    return message

print('\n {}'.format(message))
print(change_function('I passed a sentence instead of a word.'))
print(message)
# Global Scope: Variables defined outside of any function, at the top level of a script or module, have a global scope. They can be accessed from anywhere within the program, including inside functions. However, if a function tries to modify a global variable, it must explicitly declare the variable as global using the global keyword.
# default parameters
def addition(a=3,b=9,c=11):
    return a+b+c
print(f'addition() function return: {addition()}')

# Argument list parameter. The *args syntax in a function definition allows you to pass a variable number of positional arguments to the function. It collects all the positional arguments into a tuple inside the function.

def loop_args(*args):
    for arg in args:
        print(arg)
        
args_list = [1,4,6,0,2,319,23,-12]
loop_args(args_list)
print()
# **kwargs: The **kwargs syntax in a function definition allows you to pass a variable number of keyword arguments (or named arguments) to the function. It collects all the keyword arguments into a dictionary inside the function.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(a=1, b=2, c=3)  # Output: a: 1, b: 2, c: 3
my_function(name='John', age=30, city='New York')  # Output: name: John, age: 30, city: New York

# MODULE segment
import math, random as r

print("\nThe value of PI is {}".format(math.pi))

random_number = int(r.random()*10)
print("""
Welcome to the guessing Game. 
""")

guess = ''

# while random_number != guess:
#     guess = int(input("Guess the number:\n"))
    
#     if guess == random_number:
#         print("""\n{} was the correct number.
# Thank you for playing and come back next time.
#               """.format(guess))
#         break
#     else:
#         print('{} is the wrong number. Try again\n'.format(guess))
# You can always use the randrage function to create a random int number.
print(r.randrange(1,9))

# import from a module you created to use the function in that model
from new_module import checkIfEven, new_module_variable

# display the global variable in the new module
print('variable from external module: {}'.format(new_module_variable))

# use the check if even function
print(checkIfEven(27))
print(checkIfEven(24))
