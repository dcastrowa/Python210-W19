#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: Mailroom_Part_2
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 02/03/2019
# ----------------------------------------------------------------------- #

import sys, io, os


# -------------------- DATA -------------------- #

donors = {}
donors['Kevin Cavanaugh'] = (500.55, 899.34, 78.94)
donors['Victor Murphy'] = (99.89, 87.02)
donors['Randy Brown'] = (10.11, 1000.01, 99.99)
donors['Piper Long'] = (190.99, 100.02)
donors['Kim Pinkie'] = (2344.44, 8999.66, 345.55)

prompt = "\n".join(("What would you like to do?",
                    "1. Send a Thank You to single donor",
                    "2. Create a Report",
                    "3. Send letters to all donors",
                    "4. Quit"))


def send_thank_you(name, donation):
    letter = '\n Dear {}, \n\n Thank you for the generous donation of ${:.2f}. \n We are very grateful for your' \
             ' donation. \n\n Sincerely, \n The Team'.format(name, donation)
    return letter + '\n'


def add_donation(record, person, donation):
    if person in record:
        record[person] += donation,
    else:
        record[person] = donation,


def donor_stats(donor):
    total = sum(donors[donor])
    num_donations = int(len(donors[donor]))
    avg_donation = int(total / num_donations)
    return '{:<20} ${:<15.2f} {:<10} ${:<15.2f} '.format(donor, total, num_donations, avg_donation)


def create_report():
    print('{:<20} |{:<15} |{:<10} |{:<15} '.format('Donor', 'Total', 'Num Gifts', 'Average Gift'))
    print('-' * 60)
    for donor in donors:
        print(donor_stats(donor))
    print('\n')


def write_letters():
    cwd = os.getcwd()
    os.mkdir('thank_you_letters')
    os.chdir('thank_you_letters')

    for donor in donors.keys():
        file_name = ('thank_you_{:s}.txt'.format(donor))
        open(file_name, 'a').close()
        file = io.open(file_name, 'w')
        file.write(send_thank_you(donor, donors[donor][len(donors[donor]) - 1]))
        file.close()

    os.chdir(cwd)


def main():

    while True:
        response = input(prompt)
        if response == "1":
            name = input('Enter name of donor: ').lower()
            if name == 'list':
                for donor in donors.keys():
                    print(donor)
                continue
            else:
                try:
                    donation = float(input('How much did {:s} donate?'.format(name)))
                    add_donation(donors, name, donation)
                except ValueError:
                    continue
                else:
                    if donation <= 0:
                        print('Donations must be greater than $0\n')

            print(send_thank_you(name, donors[name][len(donors[name]) - 1]))
            continue

        elif response == "2":
            create_report()

        elif response == "3":
            write_letters()

        else:
            input('Press Enter to quit :)')
            break


if __name__ == "__main__":
    main()
