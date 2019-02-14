#!/usr/bin/env

# ----------------------------------------------------------------------- #
# Title: Dictionaries_LAb
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & started lab, 2/1/19
# ----------------------------------------------------------------------- #
print('='*40)
print('DICTIONARIES_1')
print('='*40)

cake_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(cake_dict)

cake_dict.pop('cake')

print(cake_dict)

cake_dict['fruit'] = 'mango'

print(cake_dict)

if 'cake' in cake_dict.keys():
    print('T')
else:
    print('F')

if 'mango' in cake_dict.values():
    print('T')
else:
    print('F')

print('='*40)
print('DICTIONARIES_2')
print('='*40)

new_dict = dict()
for value in cake_dict.values():
    num_of_ltr = value.lower().count('t')
    new_dict[value] = num_of_ltr
print(new_dict)


print('='*40)
print('SETS_1')
print('='*40)

s2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
s3 = {3, 6, 9, 12, 15, 18}
s4 = {4, 8, 12, 16, 20}

print('\n', s2, '\n', s3, '\n', s4)

if s3 < s2:
    print('T')
else:
    print('F')

if s4 < s2:
    print('T')
else:
    print('F')

print('='*40)
print('SETS_2')
print('='*40)

python_set = {'p', 'y', 't', 'h', 'o', 'n'}

python_set.add('i')

frozen_set = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))

print('This is the union:', '\n', (python_set | frozen_set), '\n')

print('This is the intersection:', '\n', python_set.intersection(frozen_set))
