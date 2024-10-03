import random


# 1. Write a generator function that takes a list of numbers and yields only the
# even numbers from the list.
def generate_even(numbers):
    for nr in numbers:
        if nr % 2 == 0:
            yield nr


def get_even_list(numbers):
    even_numbers = []
    for nr in numbers:
        if nr % 2 == 0:
            even_numbers.append(nr)
    return even_numbers


# 2. Create a generator function that receives a parameter max_nr and yields a
# random number between 1 and max_nr, indefinitely
def generate_random_number(max_nr):
    """Generator function that yields random numbers between 1 and max_nr
    indefinitely"""
    while True:
        yield random.randint(1, max_nr)


# 3. Write a generator function that yields unique elements from an iterable
# received as parameter.
def generate_unique_elements(it):
    unique = []
    for elem in it:
        if elem not in unique:
            yield elem
            unique.append(elem)


def generate_unique_elements_v2(it):
    for elem in set(it):
        yield elem


if __name__ == '__main__':
    l = [3, 6, 2, 12, 45, 87, 18, 37, 94]
    print(f'Even numbers in {l}:')
    for i in generate_even(l):
        print(i)

    # By using an infinite generator, we have the option to decide when using it
    # how many iterations we need
    random_number_generator = generate_random_number(100)
    print('Generating 5 random numbers by calling next() on the generator object:')
    for _ in range(5):
        print(next(random_number_generator))

    print('Generating 7 random numbers by iterating on the generator object:')
    count = 0
    for random_number in random_number_generator:
        print(random_number)
        count += 1
        if count == 7:
            break

    print('Generating unique numbers from a list:')
    for i in generate_unique_elements([5, 7, 1, 3, 1, 3, 5, 5]):
        print(i)

    print('Generating unique elements from a string:')
    for i in generate_unique_elements('hello'):
        print(i)

    print('Generating unique elements from another iterator:')
    # iter(tuple) will return an iterator that yields elements from the tuple
    for i in generate_unique_elements(iter(('ana', 'ana', 'are', 'mere', 'mere'))):
        print(i)
