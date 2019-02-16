#!/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Mail Room Part 4
# Change log: (Who, When, What)
# dcastrowa, 02/16/2019, created file
# ----------------------------------------------------------- #
import os
import io
import sys

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
    """
    Creates a template email to send to donors.
    :param (str) name: name of donor
    :param (int) donation: dollar amount for donation
    :return (str): complete template email
    """
    letter = ('Dear {}:\nThank you for donating ${}.\n'
              'We appreciate your contribution!\n\n\n\n'
              'Sincerely,\n'
              'DonationCentral Inc.'.format(name, donation))
    return letter


def write_letters():
    """
    Writes out new .txt files to created directory
    :return: no return
    """
    cwd = os.getcwd()
    try:
        os.mkdir('ThankYouLetters')
        os.chdir('ThankYouLetters')
    except FileExistsError:
        print('File already exists. Create new directory.')
        new_dir = input('New directory name: ')
        os.mkdir(new_dir)
        os.chdir(new_dir)

    for name, donation in donors_db.items():
        file_name = ('ThankYou{}.txt'.format(name.replace(' ', '')))
        open(file_name, 'a').close()
        new_file = io.open(file_name, 'w')
        new_file.write(create_email(name, int(donation[-1])))
        new_file.close()

    os.chdir(cwd)


def list_of_donors():
    donors_listing = 'DONORS: \n'
    donors_listing += format_line + '\n'
    for key in donors_db.keys():
        donors_listing += key + '\n'
    donors_listing += format_line
    return donors_listing


def thank_you():
    response = input('list -- view all donors\n'
                     'first name last name -- add new donation\n')
    while True:
        if response == 'list':
            print(list_of_donors())
            break
        else:
            try:
                donation_amount = int(input('Enter donation amount: $'))
                add_donation(response, donors_db, donation_amount)
                print(create_email(response, donation_amount))
                break
            except ValueError:
                print('Enter a number value')


def add_donation(response, record, donation):
    if response in record:
        record[response] += donation,
    else:
        record[response] = donation,
    return record


def get_report(database):
    final_report = '{:<25}{:<25}{:<25}{:<25}\n'.format('Donor', 'Average', 'Num of Gifts', 'Total')
    final_report += '=' * 100 + '\n'
    for name, amounts in database.items():
        final_report += '{:<25}${:<25.2f}{:<25}${:<25}\n'.format(name, sum(amounts) / len(amounts), len(amounts),
                                                                 sum(amounts))
    final_report += '=' * 100
    return final_report


def display_report():
    print(get_report(donors_db))


def quit_program():
    input('Press enter to quit.')
    return sys.exit()


def user_response(choice):
    options = {'1': thank_you,
               '2': display_report,
               '3': write_letters,
               '4': quit_program}
    return options.get(choice)()


def main():
    while True:
        try:
            response = input(prompt_msg)
            user_response(response)
        except:
            print('Not an option. Enter a valid response.')


if __name__ == '__main__':
    main()

