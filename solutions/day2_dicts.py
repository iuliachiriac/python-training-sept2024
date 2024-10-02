# 1.Create a dictionary called my_dict that contains the following key-value
# pairs:
my_dict = {
    "name": "John",
    "age": 30,
    "occupation": "developer",
    "city": "New York",
}
# Print the entire my_dict to the console.
print('Initial dictionary:', my_dict)
# Use the get() method to print the value associated with the key "occupation"
# to the console.
print('Occupation:', my_dict['occupation'])
# Add a new key-value pair to my_dict that represents John's salary. Set the
# salary to 75000.
my_dict['salary'] = 75000
# Modify the value associated with the key "city" to be "San Francisco".
my_dict["city"] = 'San Francisco'
# Print the entire my_dict to the console again to see the changes.
print('Changed dictionary:', my_dict)
# Use the pop() method to remove the key-value pair associated with the key
# "occupation" from my_dict.
my_dict.pop('occupation')
# Create a new dictionary called friend_dict that contains the following
# key-value pairs:
friend_dict = {
    "name": "Emily",
    "age": 28,
    "occupation": "teacher",
    "city": "Los Angeles",
}
# Use the update() method to add all the key-value pairs from friend_dict to
# my_dict.
my_dict.update(friend_dict)
# Print the entire my_dict to the console again to see the changes.
print('Updated dictionary:', my_dict)
# Use a for loop to iterate over the items in my_dict and print each key and
# its associated value to the console.
for key, val in my_dict.items():
    print(f"{key:<12}{val}")


# 2. Given the following dictionary:
d = {
  'times': 100,
  'name': 'George',
  'hobbies': ['fishing', 'hiking'],
}
# add key 'friends' to d with ['Andrei', 'Mihai', 'Alina'] as value
names = ['Andrei', 'Mihai', 'Alina']
d['friends'] = names
print('Dictionary after adding "friends":', d)

# sort value for key 'friends'
d['friends'].sort()
# It's the same with calling: names.sort() because `d['friends'] is names`
# assert verifies a conditions and raises AssertionError if condition is False
assert d['friends'] is names

print('Dictionary after sorting "friends":', d)
print('Names list is also sorted:', names)

# remove 'hiking' from hobbies list
d['hobbies'].remove('hiking')
print('Dictionary after removing hobby:', d)

# remove 'times' key from d
del d['times']
print('Dictionary after removing "times" key:', d)

# 3. Given a list of strings build a dictionary that has each unique string as a
# key and the number of appearances as a value
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there', 'hello']
# Version 1
occurrences = {}
for word in set(words):
    occurrences[word] = words.count(word)
print(occurrences)

# Version 1.5 (dict comprehension)
print({word: words.count(word) for word in set(words)})

# Version 2
occurrences = {}
for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1
print(occurrences)

# Version 3
occurrences = {}
for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1
print(occurrences)

# 4. Create a dictionary of dictionaries to store the following data
d = {
    1: {"interface": "Ethernet0", "ip": "1.1.1.1", "status": "up"},
    2: {"interface": "Ethernet1", "ip": "2.2.2.2", "status": "down"},
    3: {"interface": "Serial0", "ip": "3.3.3.3", "status": "up"},
    4: {"interface": "Serial1", "ip": "4.4.4.4", "status": "up"},
}

# Write a python program to find the status of a given id
interface_id = 3
print(f'Status of id={interface_id}:', d[interface_id]['status'])

# Write a python program to find interface and IP of all interfaces which are up
print('Interfaces that are up:')
for int_id, row in d.items():
    if row['status'] == 'up':
        print(row['interface'], row['ip'])

# Write a python program to count how many ethernet interfaces there are
ethernet_count = 0
for int_id, row in d.items():
    if row['interface'].startswith('Ethernet'):
        ethernet_count += 1
print('Number of ethernet interfaces:', ethernet_count)

# Write a python program to add a new entry to the dictionary
# (auto-increment the id)
next_id = max(d.keys()) + 1
d[next_id] = {"interface": "Ethernet3", "ip": "1.2.3.4", "status": "down"}
print('Dictionary after adding new entry:', d)
