# Making the porgram interactive via console
# Python allows for user interaction through the input() function, which prompts the user to enter data via the console, typically used for simple text-based input. This input can then be stored in variables or used directly within the program for processing, making Python programs interactive and adaptable to user input.
# userName = input('Hello User. What is Your name?\n')
# program_language = input('What is your programming language of choice?\n')
# year_len = int(input('How many years have you been programming?\n'))

# print("Welcome to the Python World {}.\n You have been programming for {} years and your programming language of choice is {}.".format(userName, year_len,program_language))


# Conditional Statement - in Python allow for decision-making within programs, executing different blocks of code based on certain conditions. 
# if, elif, else statement
x = 2

if x == 2:
    print('The value you enter is {}'.format(True))
    
    
number = int(input('Enter a number from 1-10\n'))

if number == 0:
    print('You enter {}. That is neither and even or odd number.'.format(number))
elif number%2 == 0:
    print('You enter an Even number.')
else:
    print('You enter an Odd number.')

# For Loop
# A for loop in Python is used to iterate over a sequence of elements such as lists, tuples, strings, or other iterable objects
# create a list with week days value
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# iterate through with for loop
print('\nThe days in a week are:')
for day in weekdays:
    print(day)
# the number of iteration is predicated based on the iterable refernce.
# for a in iterable: print(a)
# loop through a dictionary
random_dict = {'a':1,'b':2, 'c':3, 'd':4}
for key, value in random_dict.items():
    print('Key: {} - Value: {}'.format(key, value))
    
# Loop through a string
for letter in 'Antidisestablis':
    print('letter: {}.'.format(letter))
    
# you can also use the range() function to iterate in sequence range(start, end, step)
# print out all odd numbers by using the step in range
print('\nOdd Numbers:')
for i in range(1,10,2):
    print(i)
    
# while loop
# A while loop in Python repeatedly executes a block of code as long as a specified condition is true
counter = 5

while counter > 0:
    print('Counter: {}'.format(counter))
    counter-=1

print('\n')
# If you wnat to break any of the loops you can utilize the reserve keyword 'break'
j= 0
for i in range(5):
    j = j+2
    print('i: {}, j = {}.'.format(i,j))
    if j == 6:
        print('The loop is broken.\n')
        break
    
# if you only want to skip a iteration and not break it use the continue key workd

for x in range(10):
    if x == 7:
        continue
    
    print(x)
print()

# Try except
# The try block in Python contains code that may raise an exception. If an exception occurs within the try block, the control is transferred to the except block, where you can handle the exception. This allows you to gracefully handle errors and prevent them from crashing the program.
try:
    answer = 12/0
    print('{} / {} = {}.'.format(12,0,answer))
except:
    print("An error occured")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    