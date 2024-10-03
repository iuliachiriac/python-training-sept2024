import string


# 1. Write a list comprehension that creates a list of numbers from 1 to 20 that
# are divisible by 3.
print([nr for nr in range(1, 21) if nr % 3 == 0])

# 2. Write a list comprehension that creates a list of all the vowels in a given
# string.
s = "comprehension"
print([char for char in s if char in "aeiouy"])

# 3. Write a list comprehension that creates a list of all the words in a given
# string that have more than 3 letters.
s = "comprehension that creates a list of all the words in a given"
print([word for word in s.split() if len(word) > 3])


# 4. Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord
# built-in to obtain ASCII code. Keys range from "a" to "e".
d1 = {letter: ord(letter) for letter in string.ascii_letters if letter <= 'e'}

# 5. Using the dictionary generated above, create another one where you swap
# keys and values.
d2 = {ascii_code: letter for letter, ascii_code in d1.items()}

# 6. Filter the above dictionary to contain only even keys.
d3 = {
    ascii_code: letter
    for ascii_code, letter in d2.items()
    if ascii_code % 2 == 0
}

# 7. Can you obtain dictionary from ex. 3 from the given string ("abcde") in a
# single dict comprehension?
d4 = {
    ord(letter): letter
    for letter in string.ascii_letters[:5]
    if ord(letter) % 2 == 0
}

print(d1)
print(d2)
print(d3)
print(d4)
