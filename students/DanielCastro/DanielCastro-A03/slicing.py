# Title: Slicing
# Change log: (Who,When, What)
# dcastrowa, 01/26/19, created slicing file with functions

my_string = 'do stuff with this string'
my_tuple = (2, 5, 56, 23, 45, 4, 72, 34, 25, 12, 39)


def exchange_first_last(sequence):  # with the first and last items exchanged.
    try:
        first = sequence[-1],
        middle = sequence[1:-1]
        last = sequence[0],
        return first + middle + last
    except TypeError:
        first = sequence[-1]
        middle = sequence[1:-1]
        last = sequence[0]
        return first + middle + last


def every_other_item(sequence):  # with every other item removed.
    return sequence[::2]


def remove_four(sequence):  # first 4 and last 4 items removed and then every other item in the remaining sequence.
    return sequence[4:-4:2]


def reverse_sequence(sequence):  # with the elements reversed (just with slicing).
    return sequence[::-1]


def thirds_sequence(sequence):  # with the last third, then first third, then the middle third in the new order.
    thirds = int(len(sequence) / 3)
    last = sequence[-thirds:]
    first = sequence[:thirds]
    middle = sequence[thirds:-thirds]
    return last + first + middle


print('My tuple = {}'.format(my_tuple))
print('-' * 40)
exchange_test = exchange_first_last(my_tuple)
print('Exchange first and last')
print(exchange_test)
print('-' * 40)
every_other_test = every_other_item(my_tuple)
print('Every other item')
print(every_other_test)
print('-' * 40)
remove_four_test = remove_four(my_tuple)
print('Remove four first/last and print every other')
print(remove_four_test)
print('-' * 40)
thirds_test = thirds_sequence(my_tuple)
print('Thirds')
print(thirds_test)
