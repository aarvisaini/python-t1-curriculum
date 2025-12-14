nums = [1, 2, 3]
print(nums)

biggest_item = max(nums)
smallest_item = min(nums)

# You can use built-in Python functions to find the biggest and smallest items.
print("The biggest item:", biggest_item)
print("The smallest item:", smallest_item)

print("Our algorithm:")

nums2 = [5, 6, 7]

biggest = nums2[0] # Start by assuming the first item is the biggest.
for i in range(len(nums2)): # Go through each item in the list
    if nums2[i] > biggest: # If we find something bigger, update our guess.
        biggest = nums2[i]

print("The biggest item:", biggest)

nums3 = [21, 34, 67]

smallest = nums3[0]
for i in range(len(nums3)):
    if nums3[i] < smallest:
        smallest = nums3[i]

print("The smallest item:", smallest)

# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
total_sum = 0
for num in numbers:
    total_sum += num
print("Total sum:", total_sum)      

# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print("Biggest number:", biggest)

# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]
negative_sum = 0
for num in numbers:
    if num < 0: 
        negative_sum += num
print("Sum of negative numbers:", negative_sum) 

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
even_sum = 0
for num in numbers:
    if num % 2 ==0: 
        even_sum += num
print("Sum of even numbers:", even_sum)

# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]
negative_numbers = [num for num in numbers if num < 0]
if negative_numbers:
    biggest_negative = max(negative_numbers)
    print("Biggest negative number:", biggest_negative)
else:
    print("No negative numbers found.")