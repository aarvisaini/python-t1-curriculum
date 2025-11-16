# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
print("Problem 1: Print Even if the number is divisible by 2, otherwise print Odd")
User_num = int(input("Give me a number: ")) 
if (User_num % 2):
    print("Odd")
else:
    print("Even")

# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
print("Problem 2: Print Weekend for saturday/sunday, else print Weekday")
day = input("What day of the week is it?:")

if day == "monday":
    print("weekday")
elif day == "friday":
    print("weekday") 
elif day == "saturday":
    print("weekend")
elif day == "sunday":
    print("weekend")
elif day == "tuesday":
    print("weekday")
elif day == "wednesday":
    print("weekday")   
elif day == "thursday":
    print("weekday")

# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
print("Problem 3: Guess the random number between 1 and 10")


import random

random_number = random.randint(1, 10)
#print(random_number)
User_random_guess = int(input("Guess a number between 1 and 10: "))
if (User_random_guess == random_number):
    print("Correct!")
else:
    print("Try again!")

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
print("Problem 4: Check if the positive integer is a big even number")
User_positive_int = int(input("Give me a positive integer: ")) 
if (User_positive_int % 2 == 0) and (User_positive_int > 10):
    print("Big even number")        
else:
    print("Number does not meet criteria")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
print("Problem 5: is there a larger number or are they equal?")
User_num1 = int(input("Give me first number: ")) 
User_num2 = int(input("Give me second number: ")) 
( User_num1 != User_num2 )
if (User_num1 == User_num2):
   print("Numbers are equal")
elif (User_num1 < User_num2):
    print("Larger number is:", User_num2)
else:
    print("Larger number is:", User_num1)