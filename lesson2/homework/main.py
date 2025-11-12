
My_lucky_number = 6
print(My_lucky_number)

My_height_in_meters = 1.3
print(My_height_in_meters)

My_favorite_animal = "Fawn"
print (f"My favorite animal is: {My_favorite_animal}" )

My_name = "Aarvi"
My_favorite_color = "pink"
My_age = 9
print(f"{My_name}'s age is {My_age} and favorite color is {My_favorite_color}. ")

My_first_name ="Aarvi"
My_last_name ="Saini"
print(My_first_name)
print(My_last_name)

How_long_I_Sleep = "10 hours"
print(How_long_I_Sleep)

My_favorite_fruit = "mango"
print(f"My favorite fruit is {My_favorite_fruit}")

My_city = "Seatle"
My_country = "U.S.A"
print(My_city )
print(My_country)

My_dog_name = "Ruby"
My_dog_age = 3
My_dog_type= "Pomarian"
print(f"My dog's name is {My_dog_name} it's age is {My_dog_age } and it's a type of {My_dog_type}.")

people_at_restraunt = 10
name_of_restraunt = "Canam pizza"
print(f" At {name_of_restraunt} {people_at_restraunt} people are eating food." )

num_string = "42"
num_integer = int(num_string)  # Convert string to integer
print(num_integer + 1)

float_string = "3.14"
num_float = float(float_string)
print(num_float +2.7)

int_num = 7
float_num = float(int_num)
print(float_num -2)

# input ALWAYS returns a string
user_input = input("Give me an integer: ")

# Error: cannot add an integer to a string
# print(user_input+1)

number = int(user_input)  # casting to an integer

# You can shorten this process:
user_number = int(input("Give me a number: "))
print(user_number + 1)

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")
	
user_pushups = int(input("How many pushups can you do: ")) 
(user_pushups * 7)
print(f"Aarvi can do {user_pushups * 7} pushups in a week.")

user_num1 = int(input("give me a number1: ")) 
user_num2 = int(input("give me a number2: ")) 
Remainder = user_num1 % user_num2
Quotient =  user_num2 // user_num1
print(Remainder)
print(Quotient)

User_animal = (input("What is your favorite animal: "))
User_color = (input("What is your favorite color: "))
print("What is your favorite color: ")
print("What is your favorite animal: ")
print(f"It would be cool if there was a {User_color}{User_animal}!")
