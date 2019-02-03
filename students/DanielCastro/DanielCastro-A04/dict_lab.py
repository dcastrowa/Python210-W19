# !/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Dictionary Lab
# Change log: (Who, When, What)
# dcastrowa, 02/02/2019, created file
# ----------------------------------------------------------- #

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
my_dict = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s = set(range(21))
s2 = set()
s3 = set()
s4 = set()
python_set = set('python')
frozen_marathon = frozenset('marathon')


def print_dict(your_dict):  # Display the dictionary.
    print(your_dict)


def delete_entry(your_dict):  # Delete the entry for “cake”.
    your_dict.pop('Cake')
    print_dict(your_dict)     # Display the dictionary.


def add_entry(your_dict):  # Add an entry for “fruit” with “Mango” and display the dictionary.
    your_dict['Fruit'] = 'Mango'
    print(your_dict.keys())  # Display the dictionary keys.
    print(your_dict.values())  # Display the dictionary values.
    print('Is "Cake" a dictionary key?')
    if 'Cake' in your_dict.keys():  # Display whether or not “cake” is a key in the dictionary
        print('True')
    else:
        print('False')
    print('Is "Mango" a dictionary value?')
    if 'Mango' in your_dict.values():  # Display whether or not “Mango” is a value in the dictionary
        print('True')
    else:
        print('False')


def count_letters(letter, your_dict):  # Make a dictionary using the same keys but with the number of ‘t’s
    new_dict = dict()
    for value in your_dict.values():
        num_of_letters = value.lower().count(letter)
        new_dict[value] = num_of_letters
    print(new_dict)


def divide_by(num, num2):
    return num / num2


def create_set(origin_set, div_num, new_set):
    for num in origin_set:
        new_num = divide_by(num, div_num)
        new_num = round(new_num, 2)
        new_set.update([new_num])
    print(new_set)


def main():
    print('DICTIONARIES 1:')
    print('=' * 75)
    print('Display dictionary:')
    print_dict(my_dict)
    print('-' * 75)
    print('Remove "cake" entry:')
    delete_entry(my_dict)
    print('-' * 75)
    print('Add fruit entry:g')
    add_entry(my_dict)
    print('-' * 75)
    print('DICTIONARIES 2:')
    print('=' * 75)
    count_letters('t', my_dict)
    print('-' * 75)
    print('SETS 1:')
    print('=' * 75)
    create_set(s, 2, s2)
    create_set(s, 3, s3)
    create_set(s, 4, s4)
    print('s3 subset of s2: {}'.format(s3.issubset(s2)))
    print('s4 subset of s2: {}'.format(s4.issubset(s2)))
    print('-' * 75)
    python_set.add('i')
    print('Add "i": {}'.format(python_set))
    print('Union: {}'.format(python_set.union(frozen_marathon)))
    print('Intersection: {}'.format((python_set.intersection(frozen_marathon))))


if __name__ == '__main__':
    main()
