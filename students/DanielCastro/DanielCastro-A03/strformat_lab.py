# !/usr/bin/env python3

# ------------------------------------------------ #
# Title: String Format Lab
# Change Log: (Who,What,When)
# dcastrowa, created file, 01/28/19
# ------------------------------------------------ #

num1 = 2
num2 = 123.4567
num3 = 10000
num4 = 12345.67
nums_tuple = (num1, num2, num3, num4)
another_tuple = (1, 2, 3, 4, 5)
t4_tuple = (4, 30, 2017, 2, 27)
t5_list = ['orange', 1.3, 'lemon', 1.1]
row1 = ['23', 'Bob', '$20.50']
row2 = ['34', 'Ana', '$45.25']
row3 = ['2', 'Jay', '$30.5']
table = [row1, row2, row3]


def formatter(in_tuple):
    form_string = 'The {} numbers are: '.format(len(in_tuple)) + '{:d} ' * len(in_tuple)
    return form_string.format(*in_tuple)


print("TASK 1")
print('file_{:0>3d} : {:.2f}, {:.2e}, {:.3e}'.format(2, 123.4567, 10000, 12345.67))
print('=' * 50)

print("TASK 2")
print(f'file_{num1:0>3d} : {num2:.2f}, {num3:.2e}, {num4:.3e}')
print('=' * 50)

print('TASK 3')
task3 = formatter(another_tuple)
print(task3)
print('=' * 50)

print('TASK 4')
print('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(*t4_tuple))
print('=' * 50)

print('TASK 5')
print(f'The weight of an {t5_list[0].capitalize()} is {t5_list[1] * 1.2} and the weight of a {t5_list[2].capitalize()}'
      f' is {t5_list[3] * 1.2}')
print('=' * 50)

print('TASK 6')
print('{:<5} {:<5} {:<5}'.format('Age', 'Name', 'Cost'))
for row in table:
    print('{:<5} {:<5} {:<5}'.format(*row))
