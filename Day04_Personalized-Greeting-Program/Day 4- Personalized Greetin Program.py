# Learning objects
# What are variables?
# Data types: Strings, integers, floats and booleans
# Type conversion
# string  formating
# Day 2 projects

# What are Variables: Variables are containers where data can be stored.
name = "Oluwademilade"
age = 42 

# Data Types
# String
name = "Oluwademilade"

# integer
age = 42

# Float
height = 5.8

# boolean
is_student = False


# Type Conversion
age = "17"
my_age = int(age)
print(my_age + 5)

#you can also have
example = "17"
example_integer = int(example)
example_float = float(example)
example_sting = str(example_integer)


#String Formatting
name = "oluwademilade"
# + formatting
print("Hello, " + name + "!")
# 
print("Hello my friend! {}!".format(name))
# fstring formatting
print(f"Hello my friend {name}")

#Project
# Personalized greting Program

#Step 1: ask for detials
name = input("What is your name? ")
age = int(input("How old are you"))
colour = input("What's your favourite colour")

#Step 2: Generte a personalized greeting Message
print("\n---- Personalized Greeting ----")
print(f"Greetings {name}, happy to have you here")
print(f"you are {age}, You're getting mature, aren't you🙌")
print(f"Oh wow, {colour} is your favourite colour, great choice")
print("You're ready for this python journey, let's get this bread")