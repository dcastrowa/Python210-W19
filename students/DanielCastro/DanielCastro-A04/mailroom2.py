#!/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Mail Room Part 2
# Change log: (Who, When, What)
# dcastrowa, 02/03/2019, created file
# ----------------------------------------------------------- #
import os
import io

# Create list of donors
donors_db = {'Bob Belcher': (400.50, 250.46),
             'Peter Griffin': (865.23, 910.06, 454.25),
             'Charlie Brown': (420.45, 250.67),
             'Scooby Doo': (2000.60, 500.84),
             'Luke Skywalker': (340.55, 67.89, 900.00)}

prompt_msg = '\n'.join(('Enter a # option:',
                        '1 -- Send a Thank you',
                        '2 -- Create a Report',
                        '3 -- Send letter to all donors',
                        '4 -- quit',
                        ''))

format_line = ('=' * 75)


def create_email(name, donation):
        letter = ('Dear {}:\nThank you for donating ${}.\n'
                  'We appreciate your contribution!\n\n\n\n'
                  'Sincerely,\n'
                  'DonationCentral Inc.'.format(name, sum(donation)))
        return letter


def write_letters(data_set):
    cwd = os.getcwd()
    os.mkdir('ThankYouLetters')
    os.chdir('ThankYouLetters')

    for name, donation in data_set.items():
        file_name = ('ThankYou{}.txt'.format(name.replace(' ', '')))
        open(file_name, 'a').close()
        new_file = io.open(file_name, 'w')
        new_file.write(create_email(name, donation))
        new_file.close()

    os.chdir(cwd)


def thank_you():
    while True:
        response = input('list -- view all donors\n'
                         'first name last name -- add new donation\n')
        if response == 'list':
            print('DONORS: ')
            print(format_line)
            for key in donors_db.keys():
                print(key)
            print(format_line)
        elif response in donors_db:
            donation_amount = float(input('Enter donation amount: $'))
            donors_db[response] += donation_amount,
            break
        else:
            donation_amount = float(input('Enter donation amount: $'))
            donors_db[response] = donation_amount,
        #     print(names)
        #     continue
        # elif response not in names:
        #     donor_db.append([response.title()])
        #     donation_amount = float(input('Enter donation amount: '))
        #     donor_db[-1].append(donation_amount)
        #     print('Thank you, {} for donating ${:.2f}'.format(donor_db[-1][0], donor_db[-1][1]))
        #     break


def report():
    print('{:<25}{:<25}{:<25}{:<25}'.format('Donor', 'Average', 'Num of Gifts', 'Total'))
    print('=' * 100)
    for name, amounts in donors_db.items():
        print('{:<25}${:<25.2f}{:<25}${:<25}'.format(name, sum(amounts)/len(amounts), len(amounts), sum(amounts)))
    print('=' * 100)


def quit_program():
    input('Press enter to quit.')
    pass


def user_choice(choice):
    switch_func_dict = {1: thank_you(),
                        2: report(),
                        3: write_letters(donors_db),
                        4: quit_program()}
    return switch_func_dict.get(choice, 'NA')


def main():
    while True:
        response = input(prompt_msg)
        if response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            write_letters(donors_db)
        elif response == '4':
            input('Press enter to quit.')
            break
        else:
            print('Not an option. Choose 1-4')


if __name__ == '__main__':
    main()

