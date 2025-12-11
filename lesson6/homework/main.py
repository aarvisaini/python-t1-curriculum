# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names)
print("Problem 1")
print(names.count("Alex"))
print(f"Alex is found {names.count('Alex')} times in the list.\n")

# Problem 2
# Search for "elephant" in the list and print if it's found.
print("Problem 2")
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
if "elephant" in animals:
    print("Elephant is found in the list.")
else: 
    print("Elephant is not found in the list.\n") 

# Problem 3
# Count and print how many scores are 100.
print("Problem 3")
scores = [95, 100, 88, 100, 77, 92]
print(scores)
count_100 = scores.count(100)
print(f"There are {count_100} scores of 100 in the list.\n")

# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
print("Problem 4")
colors = ["red", "green", "blue", "yellow"]
print(colors)
if "blue" in colors:
    index_blue = colors.index("blue")
    print(f"The color 'blue' is found at index {index_blue}.\n")
else:
    print("The color 'blue' is not found in the list.\n")

    # Problem 5
# Count and print how many temperatures in the list are below zero.
print("Problem 5")
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
temperatures_below_0 = [temp for temp in temperatures if temp < 0]
print(f"There are {len(temperatures_below_0)} temperatures below zero in the list.\n")