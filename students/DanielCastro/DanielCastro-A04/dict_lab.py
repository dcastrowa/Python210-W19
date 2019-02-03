# !/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Dictionary Lab
# Change log: (Who, When, What)
# dcastrowa, 02/02/2019, created file
# ----------------------------------------------------------- #

# Create a dictionary containing
# “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
my_dict = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}


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


def count_letters(letter, your_dict):
    for value in your_dict.values():
        counter = 0
        for char in value:
            if char.lower() == letter.lower():
                counter += 1
        print('{} - Number of {}\'s: {}'.format(value, letter, counter))


# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
# (consider upper and lower case?)


def main():
    print('DICTIONARY 1:')
    print('=' * 75)
    print('Display dictionary:')
    print_dict(my_dict)
    print('-' * 75)
    print('Remove "cake" entry:')
    delete_entry(my_dict)
    print('-' * 75)
    print('Add fruit entry:')
    add_entry(my_dict)
    print('-' * 75)
    print('DICTIONARY 2:')
    print('=' * 75)
    count_letters('t', my_dict)


if __name__ == '__main__':
    main()
