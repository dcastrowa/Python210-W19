#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: Mailroom_Part_1
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 01/29/2019
# ----------------------------------------------------------------------- #

import sys

donor1 = ['Kevin Cavanaugh', 500.55, 899.34, 78.94]
donor2 = ['Victor Murphy', 99.89, 87.02]
donor3 = ['Randy Brown', 10.11, 1000.01, 99.99]
donor4 = ['Piper Long', 190.99, 100.02]
donor5 = ['Kim Pinkie', 2344.44, 8999.66, 345.55]
donor_db = [donor1, donor2, donor3, donor4, donor5]
names = []
donation1 = []
donation2 =[]
donation3 =[]

for donor in donor_db:
    try:
        names.append(donor[0])
        donation1.append(donor[1])
        donation2.append(donor[2])
        donation3.append(donor[3])
    except IndexError:
        pass


prompt = "\n".join(("What would you like to do?",
                    "1. Send a Thank You",
                    "2. Create a Report",
                    "3. Quit"))

def send_thank_you():
    while True:
        response = input('Please enter Full Name of donor to thank: ')
        if response == 'list':
            print(names)
            continue
        elif response not in names:
            new_donor = [response]
            donor_db.append(new_donor)
            new_donation = int(input('Please enter donation amount: '))
            new_donor.append(new_donation)
            print('Thank you {} for your very generous donation of ${:.2f}'.format(new_donor[0], new_donation))
            break
    #   elif response in names:
    #   STRUGGLING WITH THiS

def create_report():
    print('{:<20} |{:<15} |{:<10} |{:<15} '.format('Donor', 'Total', 'Num Gifts', 'Average Gift'))
    print('-' * 60)
    for donor in donor_db:
        print('{:<20} ${:<15.2f} {:<10} ${:<15.2f}'.format(donor[0], sum(donor[1:]), len(donor[1:]),
            sum(donor[1:]) / len(donor[1:])))


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        else:
            input('Press Enter to quit:')
            break


if __name__ == "__main__":
    main()