# 1. Write a function filter_short_words(word_list, n) that returns the words in
# word_list shorter than n. Use filter built-in function and a lambda function.

def filter_short_words(word_list, n):
    return list(filter(lambda word: len(word) > n, word_list))


words = ["function", "test", "parameter", "class", "list"]
print("Words in", words, "shorter than 6 characters:",
      filter_short_words(words, 6))

# 2. Write a function that takes a list of tuples, where each tuple contains two
# integers, and returns a new list containing the product of the two integers in
# each tuple. Use the map function and a lambda function to implement this.
tuples = [(4, 5), (13, 6), (75, 2), (54, 11), (84, 3)]


def product_of_tuples(tuple_list):
    return list(map(lambda tup: tup[0] * tup[1], tuple_list))


print(f"Products of tuples' elements: input={tuples}, "
      f"output={product_of_tuples(tuples)}")


# 3. Write a function that takes a list of integers and returns a new list
# containing the squares of all even numbers in the original list. Use the
# filter, map, and lambda functions to implement this.
numbers = [2, 45, 6, 22, 76, 83, 1, 19, 26]


def squares_even_numbers(number_list):
    return list(map(lambda nr: nr ** 2, filter(lambda nr: nr % 2 == 1, number_list)))


print(f"Squares of even numbers in {numbers}: {squares_even_numbers(numbers)}")


# Write a function that receives any number of strings.py and returns
# the list of unique strings.py ordered by number of appearances
# (most frequent → least frequent). Use sorted built-in function.
def sort_words(*words):
    return sorted(set(words), key=words.count, reverse=True)


str_list = ['hello', 'there', 'hello', 'hi', 'hi', 'hello', 'bye']
print(f"Words in {str_list} from most frequent to least frequent:")
for elem in sort_words(*str_list):
    print(elem)
