animals = ["cat", "dog", "cat", "hamster", "parrot"] 
print(animals)

num_cats = animals.count("cat")
print("Number of cats:", num_cats)

print("Our algorithm:")

counter = 0
for i in range(len(animals)):
    item = animals[i]
    if item == "cat":
        counter = counter + 1
print(counter,"cats")

numbers = [13, 5, 7, 11, 9, 18]

counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers greater than 10")

fruits = ["apple", "banana", "orange", "apple", "kiwi", "banana", "apple"]

pets = ["dog", "cat", "dog", "hamster", "dog", "parrot"]
print(pets)
counter = 0
for pet in pets:
    if pet == "dog":
        counter += 1
print("Number of dogs:", counter) 

numbers = [8, 3, 12, 7, 4, 11]
print(numbers)
counter = 0
for number in numbers:
    if number % 2 != 0:
        counter += 1
print("Number of odd numbers:", counter)       

