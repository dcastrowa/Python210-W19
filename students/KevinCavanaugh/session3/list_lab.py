#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: List_Lab
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 01/29/2019
# ----------------------------------------------------------------------- #

import sys

# --- Series 1 --- #

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('\n'.join(fruits))

new_fruit = input('add fruit to list: ').title()
fruits.append(new_fruit)

print('\n'.join(fruits))

n = int(input('Index number of fruit you would like to view: '))
print(fruits[n - 1])

new_fruit = input('add fruit to list: ').title()
fruits = [new_fruit] + fruits

print('\n'.join(fruits))

new_fruit = input('add fruit to list: ').title()
fruits.insert(0, new_fruit)

print('\n'.join(fruits))

for i in fruits:
    if i[0] == "P":
        print(i)

# # # --- Series 2 --- #

print('\n'.join(fruits))

del fruits[-1]

print('\n'.join(fruits))

remove_fruit = input('fruit to remove from list: ')
fruits.remove(remove_fruit.title())

print('\n'.join(fruits))

# # --- Series 3 --- #


for fruit in fruits:
    do_i_like = input('Do you like {}?'.format(fruit.lower()))
    do_i_like = do_i_like.lower()
    while True:
        if do_i_like == 'yes':
            pass
        elif do_i_like == 'no':
            fruits.remove(fruit.title())
        else:
            do_i_like = input('Please input "yes" or "no".')
        break

print('\n'.join(fruits))


# --- Series 4 --- #

fruits_reversed = list()
for fruit in fruits:
    fruit_reversed = fruit[::-1]
    fruits_reversed.append(fruit_reversed.title())


print(fruits_reversed)
print(fruits)
