# Problem 1
# Write a function that returns the number 42 and print the result.
print("Problem 1")
def get_number():
    return 42
print(get_number())

# Problem 2
# Write a function that returns "penguin" and print the result.
print("Problem 2")
def get_animal():
    return "penguin"
print(get_animal())

# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
print("Problem 3")
fruit = "mango"
print(f"First fruit is: {fruit}")
def modify_fruit():
    fruit = "apple"
    print(f"Modified fruit is: {fruit}")
modify_fruit()

# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
print("Problem 4")
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"
print(full_name("Bob", "Smith"))

# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
print("Problem 5")
def calculate_perimeter(length, width):
    return 2 * (length + width)
print(calculate_perimeter(6, 7))
