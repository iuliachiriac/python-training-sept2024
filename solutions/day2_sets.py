# 1. Given the following set:
s = {6, 7}
# Add elements from [1, 2, 3] to the set
l = [1, 2, 3]
# for elem in l:
#     s.add(elem)
# s |= set(l)
s.update(l)
print('Updated set:', s)

# Print the length of the set
print('Set length:', len(s))

# Check if 4 is in the set
print('4 in set:', 4 in s)

# Remove and print an arbitrary element from the set
print('Arbitrary element:', s.pop())
print('Set after one arbitrary element:', s)

# Remove all remaining items in the set
s.clear()
print('Set after removing all elements:', s)

# 2. Create a set called fruit_set that contains the names of five different
# fruits. Add a new fruit to the fruit_set. Remove one of the fruits from the
# fruit_set. Print the new fruit_set to the console.
fruit_set = {'banana', 'apple', 'cherry', 'pineapple', 'peach'}
fruit_set.add('apricot')
fruit_set.remove('apple')
print('Fruit set after adding and removing elements:', fruit_set)


# 3. Create a set called visited_cities that contains the names of five cities
# you have visited in the past. Create a second set called bucket_list that
# contains the names of three cities you want absolutely want to visit.
visited_cities = {'Paris', 'Rome', 'Copenhagen', 'Lisbon', 'Berlin'}
bucket_list = {'Paris', 'Tokyo', 'Buenos Aires'}

# Create the set bucket_list_completed which contains cities that are in both
# visited_cities and bucket_list (intersection).
bucket_list_completed = visited_cities & bucket_list
print('Bucket list completed:', bucket_list_completed)

# Create the set all_cities which contains cities that are in either
# visited_cities or bucket_list (union).
all_cities = visited_cities | bucket_list
print('All cities:', all_cities)

# Create the set must_visit which contains cities that are in bucket_list,
# but not in visited_cities (difference).
must_visit = bucket_list - visited_cities
print('Must visit:', must_visit)

# 4. Write a Python program that counts the number of distinct words from a
# string.
# A word=a sequence of characters that is not whitespace (space, newline, tab).
my_str = """beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is better than complicated
flat is better than nested
sparse is better than dense"""

print('Distinct words in string:', len(set(my_str.split())))
