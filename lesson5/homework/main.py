# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
print("Problem 1")
car_brands = ["Toyota", "Ford", "BMW", "Honda"]
print("First brand:", car_brands[0])
print("Last brand:", car_brands[-1])
car_brands.append("Audi")
print("Updated list:", car_brands)
print()

# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
print("Problem 2")
numbers = [5, 10, 15, 20, 25]
print("Number at index 2:", numbers[2])
numbers.insert(2, 25)
print("Updated list:", numbers)
print()

# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then remove one city and print the updated list.
print("Problem 3")
cities = ["Seattle", "Dallas", "Denton"]
print("length of the list:", len(cities))
cities.remove("Dallas")
print("Updated list:", cities)
print()

# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
print ("Problem 4")
file_extensions = [".py", ".txt", ".css", ".html", ".pdf", ".java"]
import random
random_file_extensions  = random.choice([".py", ".txt", ".css", ".html", ".pdf", ".java"])
print("Random file extension:", random_file_extensions)
file_extensions.pop(3)
print("Updated list:", file_extensions)
print()

# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then count how many times a specific name appears.
print("Problem 5")
names = ["Liv", "Bob", "Pam", "Robin", "Gary", "Sam", "Bob", "Bob"]
middle_index = len(names) // 2
print("Name at middle index:", names[middle_index])    
specific_name = "Bob"
count_specific_name = names.count(specific_name)
print(f"The name '{specific_name}' appears {count_specific_name} time(s).") 
