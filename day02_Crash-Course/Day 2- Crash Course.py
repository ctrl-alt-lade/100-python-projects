# Crash Course/ Revision in preparation for 100 projects in 100 days Course
# Variables, your virtual vectors
# String Variables
name = "vivian"
# Float Variable
height = 5.8
# Integer 
age = 15
# Boolean 
is_gamer = True
# When printing, the variables can be inputed directly. Similarly, new data can be inputed to be displayed as long as it's in the double apostrophes


# Talking to the User, taking Inputs.
user_name = input("What's your name?")
print("Welcome,", user_name)

# Math Magic
# Basic Arithmetic functions can be performed on the values of variables
x = 3
y = 5

# Decision Time
age = int(input("Enter your Age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a minor")


# Loops
# Y Loop
# a Y loop is used when you want to go over something again and again until a particular scenario is left
count = 0
while count <5:
    print("Count is:", count)
    count += 1 

# Forward loop. 
# A forward loop is used when you have a list of chores and you want to go through them one by one.
video_games = ("Game 1", "Game 2", "Game 3")

 for game in video_games:
   print(game)