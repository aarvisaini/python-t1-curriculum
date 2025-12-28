# Problem 1
# Use a while loop to print the word "Python" 4 times.
print("Problem 1:")
count = 0
while count < 4:
    print("Python")
    count += 1
print()

# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
print("Problem 2:")
num = 2
while num <= 12:
    if num % 2 == 0:
        print(num)
    num += 1
print()
# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
print("Problem 3:")
user = int(input("Please enter a positive number: "))
while user <=0:
    user = int(input("That is not a positive number. Please enter a positive number: "))
count = 0
while count <= user:
    print(count)
    count += 1
print()
# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
print("Problem 4:")
start_num = int(input("Please enter a starting number greater than 10: "))
while start_num >= 0:           
    print(start_num)
    start_num -= 5  
print()            
# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
print("Problem 5:")
animals = ["dog", "cat", "horse"]
index = 0
while index < len(animals):
    print(f"A {animals[index]} is awesome!")
    index += 1
print()
