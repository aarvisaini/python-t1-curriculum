# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
print("Problem 1: sum of all the numbers greater than 25 in the list")
numbers = [10, 32, 27, 8, 50]
print("Numbers:", numbers) 
sum_greater_25 = sum(num for num in numbers if num > 25)
print(sum_greater_25)

# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
print("\nProblem 2: sum of all the numbers less than -10 in the list")
numbers = [-5, -20, -11, 0, 4, -15]
print("Numbers:", numbers)
sum_less_neg10 = sum(num for num in numbers if num < -10)
print(sum_less_neg10)   

# Problem 3
# Find and print the biggest number less than 100 in the list.
print("\nProblem 3: biggest number less than 100 in the list")
numbers = [104, 99, 86, 120, 101]
print("Numbers:", numbers)
biggest_less_100 = max((num for num in numbers if num < 100), default=None)
print(biggest_less_100)

# Problem 4
# Find and print the biggest number in the list.
print("\nProblem 4: biggest number in the list")
numbers = [12, 7, 33, 5]
print("Numbers:", numbers)
biggest = max(numbers)
print(biggest)

# Problem 5
# Find and print the total sum of all the numbers in the list.
print("\nProblem 5: total sum of all the numbers in the list")
numbers = [1, 3, 5, 7, 9]
print("Numbers:", numbers)
total_sum = sum(numbers)
print(total_sum)


