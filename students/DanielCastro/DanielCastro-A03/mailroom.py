# !/usr/bin/env python3

# ------------------------------------------------ #
# Title: String Format Lab
# Change Log: (Who,What,When)
# dcastrowa, created and completed file, 01/28/19
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
prompt_msg = '\n'.join(('Enter a # option:',
                        '1 -- Send a Thank you',
                        '2 -- Create a Report',
                        '3 -- quit',
                        ''))


def thank_you():
    response = input('Enter donor full name: ')
    for donor in donor_db:
            if response != donor:
                donor_db.append(response)

    # if response == 'list':
    #     for donor in donor_db:
    #         print(donor[0])




def main():
    response = input(prompt_msg)


if __name__ == '__main__':
    main()
