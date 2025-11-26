c = "apple"
d = "banana"
print("apple" == "apple")
print("Apple" == "apple")  # Case matters when comparing strings
print(c != d)
print("cat" > "dog")  # Alphabetical comparison when greather than and less than
print("dog" < "zebra")

day = input("What day of the week is it?:")

if day == "monday":
    print("Ugh, it's monday.")
elif day == "friday":
    print("Yay, it's almost the weekend!")
elif day == "saturday":
    print("It's the weekend!")
elif day == "sunday":
    print("It's the weekend!")
else:
    print("It's just a regular weekday.")

score = int(input("Your score out of 100: "))
if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")

User_num1 = int(input("Give me a number: ")) 
User_num2 = int(input("Give me a number: ")) 
( User_num1 != User_num2 )
if (User_num1 == User_num2):
   print("Numbers are equal")

for i in range(5):
    print("hi")

age = int(input("How old are you? "))
has_ticket = input("Do you have a movie ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes":  # AND: both conditions must be true for the statement to be true
    print("You can enter the PG-13 movie.")
else:
    print("Sorry, you can't enter.")
print("Movie check complete.")

has_pass = input("Do you have a bus pass? (yes/no) ")
has_coins = input("Do you have coins to pay? (yes/no) ")
if has_pass == "yes" or has_ticket == "yes":  # OR: at least one condition must be true for the statement to be true.
    print("You can ride the bus.")
else:
    print("You can't ride the bus.")
print("Bus check complete.")

homework_done = input("Did you do your homework? (yes/no) ")
if not homework_done == "yes":  # NOT: flips True to False and False to True.
    print("Go finish your homework!")
else:
    print("Nice job! You're all done.")
print("Homework check complete.")

# You can combine multiple logical operators.
is_raining = input("Is it raining? (yes/no) ")
has_umbrella = input("Do you have an umbrella? (yes/no)")

if is_raining == "yes" and not has_umbrella == "yes":
    print("You might get wet! Stay inside.")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside!")
else:
    print("No rain! You can go outside.")


