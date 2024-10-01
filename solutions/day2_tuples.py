# 1. Create a tuple called my_tuple that contains the following items:
# "apple", 2, True, "banana", 3.14
my_tuple = ("apple", 2, True, "banana", 3.14)
# Print the entire tuple to the console.
print('Tuple:', my_tuple)
# Print the third item in the tuple (True) to the console.
print('Third element in tuple:', my_tuple[2])
# Print the length of the tuple to the console.
print('Length of the tuple:', len(my_tuple))
# Try to change the second item in the tuple to "pear". What happens?
try:
    my_tuple[1] = "pear"
except TypeError as ex:
    print(f'Got "{ex}" when trying to change element in tuple')
# Create a new tuple called my_slice that contains only the first three items
# from my_tuple.
my_slice = my_tuple[:3]
# Print the entire my_slice tuple to the console.
print('Slice with first three elements:', my_slice)
# Use a for loop to print each item in my_tuple on a new line.
print('Printing all elements in the tuple...')
for elem in my_tuple:
    print(elem)
# Try to add a new item to my_tuple. What happens?
new_elem = 7
old_tuple = my_tuple
my_tuple += (new_elem, )
print('Adding an element to the tuple created a new object: ',
      my_tuple is not old_tuple)


# 2. Create two tuples called tuple1 and tuple2 that each contain three items of
# your choice. Combine the two tuples into a new tuple called combined_tuple.
# Print the entire combined_tuple to the console.
tuple1 = ("cat", 4, "sand")
tuple2 = (5.2, True, None)
combined_tuple = tuple1 + tuple2
print('Combined tuple:', combined_tuple)


# 3. Given two lists, create a list of tuples where element on position n is a
# tuple of elements on position n from each list.
# If one list is longer than the other, ignore extra elements.

names = ["Anna", "John", "Marie"]
ages = [12, 15, 22, 13]

tuples = []

for idx in range(min(len(names), len(ages))):
    tuples.append((names[idx], ages[idx]))

print('1. List of tuples:', tuples)


tuples = []

for idx, name in enumerate(names):
    tuples.append((name, ages[idx]))

print('2. List of tuples:', tuples)


tuples = []

for tup in zip(names, ages):
    tuples.append(tup)

print('3. List of tuples:', tuples)
