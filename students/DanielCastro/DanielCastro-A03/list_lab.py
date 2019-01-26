#!/usr/bin/env python3
fruits = ['apples', 'pears', 'oranges', 'peaches']
print(fruits)
new_fruit = input('Add your favorite fruit: ')
fruits.append(new_fruit)
print(fruits)
choose_fruit = int(input('Pick a number 1 through {}: '.format(len(fruits))))
print('You chose {}: {}'.format(choose_fruit, fruits[choose_fruit - 1]))
fruits = [input('Add another fruit: ')] + fruits
print(fruits)
fruits.insert(0, input('Add another fruit: '))
print(fruits)

for fruit in fruits:
    if fruit[0] == 'p':
        print(fruit)
