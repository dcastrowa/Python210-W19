#!/usr/bin/env python3

# ------------------------------------------------ #
# Title: String Format Lab
# Change Log: (Who,What,When)
# dcastrowa, created file, 01/28/19
# dcastrowa, completed file, 01/29/19
# ------------------------------------------------ #

# It should have a data structure that holds a list of your donors and a history of the amounts
# they have donated. This structure should be populated at first with at least five donors, with
# between 1 and 3 donations each. You can store that data structure in the global namespace.
# The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”,
# “Create a Report” or “quit”.

import sys

# Create list of donors
donor1 = ['Bobs Burger', 400.50, 250.46]
donor2 = ['Peter Griffin', 865.23, 910.06, 454.25]
donor3 = ['Charlie Brown', 420.45, 250.67]
donor4 = ['Scooby Doo', 2000.60, 500.84]
donor5 = ['Luke Skywalker', 340.55, 67.89, 900.00]
donor_db = [donor1, donor2, donor3, donor4, donor5]
names = []
donation1 = []
donation2 = []
donation3 = []

for donor in donor_db:
    try:
        names.append(donor[0])
        donation1.append(donor[1])
        donation2.append(donor[2])
        donation3.append(donor[3])
    except IndexError:
        pass

prompt_msg = '\n'.join(('Enter a # option:',
                        '1 -- Send a Thank you',
                        '2 -- Create a Report',
                        '3 -- quit',
                        ''))
format_line = ('=' * 75)


def thank_you():
    while True:
        response = input('Enter "list" or donor full name: ')
        if response == 'list':
            print('DONORS: ')
            format_line
            for donors in donor_db:
                print(donors[0])
        elif response in names:
            donation_amount = float(input('Enter donation amount: $'))
            for name in donor_db:
                if response == name[0]:
                    name.append(donation_amount)
        elif response not in names:
            donor_db.append([response.title()])
            donation_amount = float(input('Enter donation amount: $'))
            donor_db[-1].append(donation_amount)
            print('Thank you, {} for donating ${:.2f}'.format(donor_db[-1][0], donor_db[-1][1]))
            break


def report():
    print('{:<25}{:<25}{:<25}{:<25}'.format('Donor', 'Average', 'Num of Gifts', 'Total'))
    print('=' * 100)
    for name in donor_db:
        print('{:<25}${:<25.2f}{:<25}${:<25}'.format(name[0], sum(name[1:])/len(name[1:]), len(name[1:]), sum(name[1:])))


def main():
    while True:
        response = input(prompt_msg)
        if response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            input('Press enter to quit.')
            break
        else:
            print('Not an option. Choose 1-3')


if __name__ == '__main__':
    main()
