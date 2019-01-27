#!/usr/bin/env python3
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
# print('SERIES 1')
# print('=' * 40)
# print(fruits)
# new_fruit = input('Add your favorite fruit: ')
# fruits.append(new_fruit)
# print(fruits)
# choose_fruit = int(input('Pick a number 1 through {}: '.format(len(fruits))))
# print('You chose {}: {}'.format(choose_fruit, fruits[choose_fruit - 1]))
# fruits = [input('Add another fruit: ')] + fruits
# print(fruits)
# fruits.insert(0, input('Add another fruit: '))
# print(fruits)
# for fruit in fruits:
#     if fruit[0] == 'P':
#         print(fruit)
# print('=' * 40)

# print('SERIES 2')
# print('=' * 40)
# print(fruits)
# fruits.pop(-1)
# print(fruits)
# remove_fruit = input('Delete a fruit: ')
# fruits.remove(remove_fruit)
# print(fruits)
# print('=' * 40)

print('SERIES 3')
print('=' * 40)
for fruit in fruits:
    answer = input('Do you like {}? '.format(fruit.lower()))
    while answer != 'yes' or 'no':
        print('Please type "yes" or "no"')
        answer = input('Do you like {}? '.format(fruit.lower()))
