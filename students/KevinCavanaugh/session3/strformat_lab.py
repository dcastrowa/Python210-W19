#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: String_Fromat_Lab
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 01/29/2019
# ----------------------------------------------------------------------- #

# --------------------- TASK 1 --------------------- #

print('file_{:0>3d} : {:.2f}, {:.2e}, {:.3e}'.format(2, 123.4567, 10000, 12345.67))


# --------------------- TASK 2 ---------------------#

a = 2
b = 123.4567
c = 10000
d = 12345.67

print(f'file_{a:0>3d} : {b:.2f}, {c:.2e}, {d:.3e}')

# --------------------- TASK 3 ---------------------#


t = (1, 2, 4, 7, 8, 9)


def formatter(in_tuple):
    form_string = 'The {} numbers are:'.format(len(in_tuple)) + '{:d} ' * len(in_tuple)
    return form_string.format(*in_tuple)


formatted_string = formatter(t)
print(formatted_string)

# --------------------- TASK 4 ---------------------#

tuple_4 = (4, 30, 2017, 2, 27)

print('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(*tuple_4))

# --------------------- TASK 5 ---------------------#

list_5 = ['orange', 1.3, 'lemon', 1.1]
fruit_1 = list_5[0]
weight_1 = list_5[1] * 1.2
fruit_2 = list_5[2]
weight_2 = list_5[3] * 1.2

print(f'The weight of an {fruit_1.capitalize()} is {weight_1} and the weight of a {fruit_2.capitalize()} is {weight_2}')

# --------------------- TASK 6 ---------------------#

row1 = ['Kevin', '27', '$90.9']
row2 = ['Larry', '4', '$100.89']
row3 = ['Bobbie', '55', '$6.89']
row4 = ['Lillie', '12', '$187.72']
table1 = [row1, row2, row3, row4]

print('{:<10} {:<10} {:<10}'.format('Age', 'Name', 'Cost'))
for row in table1:
    print('{:<10} {:<10} {:<10}'.format(*row))
