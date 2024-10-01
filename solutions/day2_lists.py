# 1. Given the following list:
l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]

# Add [5, 7, 8] to the end of the list
l.extend([5, 7, 8])
print('Extended l:', l)
# l += [5, 7, 8]
# l[len(l):] = [5, 7, 8]
# print(l)

# Print the length of the list
print('List length:',  len(l))

# Check if 8 is in the list
print('8 in l:', 8 in l)

# Print the first position of 7 in the list
print('First position of 7 in l:', l.index(7))

# Count how many times 8 is in the list
print('Occurrences of 8 in l:', l.count(8))

# Reverse the list
l.reverse()  # The list is reversed in place, the function returns None
# l = l[::-1]
print('Reversed list:', l)

# Sort the list
l.sort()  # The list is sorted in place, the function returns None
print('Sorted list:', l)

# Remove items on last two positions and print the new list
del l[-2:]
print('List with items on last two positions removed:', l)

# 2. Write a program to create a list of the squares of the first 10 odd numbers
# by iterating through a range object.
odd_squares = []
for nr in range(1, 20, 2):
    odd_squares.append(nr ** 2)
print("Squares of the first 10 odd numbers:", odd_squares)

# 3. Write a Python program to convert a list of characters into a string.
# First solution - build the string step by step
characters = ['a', 'b', 'c', 'd']
s = ''
for char in characters:
    s += char
print('List of characters to string - v1:', s)

# Second solution - more Pythonic, uses str.join
characters = ['a', 'b', 'c', 'd']
s = ''.join(characters)
print('List of characters to string - v2:', s)


# 4. Create a list called my_list that contains the following items:
# 5, 4, 2, 3, 7, 1, 8, 9, 1, 2.
l = [5, 4, 2, 3, 7, 1, 8, 9, 1, 2]
# Create a new list called new_list that contains only the even numbers from
# my_list. Print the entire new_list to the console.
new_list = []
for elem in l:
    if elem % 2 == 0:
        new_list.append(elem)
print('Even numbers from my_list:', new_list)

# Create another new list called squared_list that contains the squares of all
# the numbers in my_list. Print the entire squared_list to the console.
squared_list = []
for elem in l:
    squared_list.append(elem ** 2)
print('Squares of all the numbers in my_list:', squared_list)

# Create a third new list called modified_list that contains each item in
# my_list multiplied by 2, but only if the original number is greater than 2.
# Print the entire modified_list to the console.
modified_list = []
for elem in l:
    modified_list.append(elem * 2 if elem > 2 else elem)
print('Items greater than 2 multiplied by 2:', modified_list)


# 5. Write a program to join together three existing lists. E.g.:
list1 = [3, 2, 5]
list2 = [4, 2]
list3 = [6, 2, 6, 1]
# output: [3, 2, 5, 4, 2, 6, 2, 6, 1]
joined_list = list1 + list2 + list3
print('Joined list:', joined_list)


# 6. Write a Python program to find the second-smallest number in a list.
numbers = [1, 1, 3, 5, 7, 3, 8, 1, 3]

# Version 1
sorted_unique_numbers = sorted(set(numbers))
print('Second smallest number - v1:', sorted_unique_numbers[1])

# Version 2
numbers.sort(reverse=True)
min_number = numbers[-1]
print('Second smallest number - v2:', numbers[numbers.index(min_number) - 1])

# Version 3
min_number = second_min_number = float('inf')
for number in numbers:
    if number < min_number:
        second_min_number = min_number
        min_number = number
    elif min_number < number < second_min_number:
        second_min_number = number
print('Second smallest number - v3:', second_min_number)


# Version 4
min_number = second_min_number = numbers[0]
for number in numbers[1:]:
    if number < min_number:
        second_min_number = min_number
        min_number = number
    elif min_number < number < second_min_number:
        second_min_number = number
print('Second smallest number - v3:', second_min_number)
