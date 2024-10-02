# 1. Write a function that takes a number as a parameter and prints its square.
def print_square(x):
    print(x ** 2)


# 2. Write another function that takes a number as a parameter and returns the
# square. Are the results of the two functions different?
def return_square(x):
    return x ** 2


ex_1_result = print_square(5)
ex_2_result = return_square(5)
print(f'Ex 1 result: {ex_1_result}\nEx 2 result: {ex_2_result}\n'
      f'Results are equal: {ex_1_result == ex_2_result}')

# 3. Are the results of the two functions above different? Which of the two
# functions can be used to compute x2 + y2 ?
x = 10
y = 3
print("Return function can be used in subsequent computations.")
print(f"Square of {x} + square of {y} = {return_square(x) + return_square(y)}")

# 4. Write a function that takes a string as an argument and returns a new
# string with all the vowels removed.

vowels = "aeiou"
vowels += vowels.upper()


def remove_vowels(text):
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text

with_vowels = "argument string vowelAA"
print(f'v1: String "{with_vowels}" without vowels: '
      f'{remove_vowels(with_vowels)}.')


def remove_vowels_v2(text):
    output = ""
    for char in text:
        if char not in vowels:
            output += char
    return output


print(f'v2: String "{with_vowels}" without vowels: '
      f'{remove_vowels_v2(with_vowels)}.')


# 5. Write a function that takes a list and an integer n as arguments and
# returns a new list that contains every n-th element from the original list.
def get_every_nth(l, n):
    if n < 1:
        raise ValueError("Works only for values greater than or equal to 1.")
    return l[n-1::n]


lst = [1, 2, 3, 5, 6, 7, 8, 1, 3, 4, 6]
print(f"Every 3rd element in {lst}: {get_every_nth(lst, 3)}")


# 6. Write a function that takes two numbers as arguments and returns their sum,
# difference, product, and quotient. Call the function and assign the result to
# 4 different variables.

def operations(x, y):
    return x+y, x-y, x*y, x//y


sum_res, diff_res, prod_res, quot_res = operations(10, 3)
print("Result of sum, difference, product, and quotient operations for 10 and "
      "3:", sum_res, diff_res, prod_res, quot_res)


# 7. Write a function that takes any number of strings.py and an integer n as
# parameters. n should be an optional parameter. Return the list of strings.py
# longer than n. By default (when n not given), it should return a list
# containing all words.

def get_longer_words(*words, n=-1):
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words


def get_longer_words_v2(*words, n=None):
    if n is None:
        return list(words)  # return early pattern
    return [word for word in words if len(word) > n]


print(get_longer_words('hello', 'hi', 'bye', n=2))
print(get_longer_words('hello', 'hi', ''))
print(get_longer_words())
print(get_longer_words(n=10))


# 8. Write a function that takes a variable number of lists as arguments and
# returns a new list that contains all the elements from all the input lists.
def chain(*lists):
    final_list = []
    for lst in lists:
        final_list.extend(lst)  # final_list += lst
    return final_list


l1 = [3, 4, 5, 6, 1]
l2 = range(10)
l3 = (4, 5, 7, 8, 9)
print(f"{l1}, {l2} and {l3} chained: {chain(l1, l2, l3)}")


# 9. Write a function that takes a variable number of keyword arguments and
# returns a new dictionary containing only the key-value pairs where the key
# starts with the letter 'a'.
def get_a_only_keys(**kwargs):
    output = {}
    for key, val in kwargs.items():
        if key.startswith('a'):
            output[key] = val
    return output


print(get_a_only_keys(ceva="altceva", aici="acolo"))  # {"aici": "acolo"}

# 10. Print a sentence using the following dictionary, the str.format method
# and ** unpacking:
country = {
    "name": "Romania",
    "population": "19 million",
    "capital": "Bucharest",
    "currency": "RON"
}
text = "{name} has a population of {population} people. The capital is " \
       "{capital} and uses {currency} as currency.".format(**country)
print(text)

# 11. Using * unpacking and range, print the numbers 1 to 20, separated by
# commas. You will have to provide an argument for print function's sep
# parameter for this exercise.

print(*range(1, 21), sep=",")

# 12. Modify your code from the previous exercise so that each number prints on
# a different line. You can only use a single print call.

print(*range(1, 21), sep="\n")
