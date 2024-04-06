#  Object-Oriented Programming (OOP) in Python is a programming approach with a paradigm that allows you to structure your code around objects, which are instances of classes. Here's a concise synopsis:

# In Python, classes are blueprints for creating objects, and objects are instances of classes that encapsulate data (attributes) and behavior (methods). OOP concepts such as encapsulation, inheritance, and polymorphism are supported in Python, allowing for modular, reusable, and maintainable code. Key OOP features in Python include defining classes with the class keyword, creating objects using constructors (__init__ method), accessing attributes and methods using dot notation, and leveraging inheritance to create hierarchies of classes. OOP in Python promotes code organization, abstraction, and code reuse, making it a powerful paradigm for building complex and scalable applications.

# Create a staff class
class Staff:
    # add content to the class
    
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self._name = pName
        self.__pay = pPay
    
    def calculate(self):
        hours = int(input("Enter the number of hours you worked this week:\n"))
        hourly_rate = int(input('Enter your hourly rate:\n'))
        self.pay = float(hourly_rate*hours)
        
        return self.__pay
    
    # create setter and getters
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Supervisor' or value == 'Employee':
            self._position = value
        else:
            print('Position Invalid. No Changes Made')
        
    
    def __str__(self):
        return """Postion = {}
Name = {}
Pay = {}\n""".format(self._position, self._name, self.__pay)


# initiliaze by creating an object of type staff
python_staff = Staff('Manager', 'James Williams', 1000)

# display the type of object and you will see the class staff
print('{}\n'.format(type(python_staff)))

print(python_staff)
python_staff.calculate()
print()
print(python_staff)
    
    
# the instance variable for the Staff class are position, name, and pay. By utilizing the object of type Staff you can have direct access to those variables
# print each variable
# print('\nCurrent Staff Variables:\n p-{}, n-{}, p-{}'.format(python_staff.position, python_staff.name, python_staff.pay))

# In other classes we have various type of modifier that dictates weather a variable should be public, private, or protected. In python the way that you make a variable private is by using the _ symbol
python_staff.position = 'Clerk'

print(python_staff.position )


python_staff.position = 'Supervisor'
# display update with the nex role
print()
print(python_staff.__str__())

# name mangling can be achieved by adding two __ sign instead of one.
# this is the error that you should see AttributeError: 'Staff' object has no attribute '__pay'
# property("Print pay: {}".format(python_staff.__pay))

# classmethod and staticmethod

class Method():
    a = 1
    @staticmethod
    def s_method():
        print('THI IS A STATIC METHOD')
        
    @classmethod
    def c_method(cls):
        print("THIS IS A CLASS METHOD: ", cls.a)
        

Method.c_method()


# Inheritance
# Parent class
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")


# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog", "bark")
        self.name = name

    def wag_tail(self):
        print(f"{self.name} wags its tail happily.")


# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat", "meow")
        self.name = name

    def purr(self):
        print(f"{self.name} purrs softly.")


# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods from both parent and child classes
dog.make_sound()  # Output: The dog makes a bark sound.
dog.wag_tail()    # Output: Buddy wags its tail happily.

cat.make_sound()  # Output: The cat makes a meow sound.
cat.purr()        # Output: Whiskers purrs softly.
