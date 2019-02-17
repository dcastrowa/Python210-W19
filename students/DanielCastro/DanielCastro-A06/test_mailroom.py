#!/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Mail Room Testing
# Change log: (Who, When, What)
# dcastrowa, 02/16/2019, created file
# ----------------------------------------------------------- #

import os
from mailroom_part4 import list_of_donors
from mailroom_part4 import add_donation
from mailroom_part4 import write_letters
from mailroom_part4 import create_email

donors_db = {'Bob Belcher': (400.50, 250.46),
             'Peter Griffin': (865.23, 910.06, 454.25),
             'Charlie Brown': (420.45, 250.67),
             'Scooby Doo': (2000.60, 500.84),
             'Luke Skywalker': (340.55, 67.89, 900.00)}


def test_write_letter():
    write_letters()
    assert os.path.isfile('ThankYou_BobBelcher.txt')


def test_create_email():
    donor_letter = create_email('Peter Griffin', 123)
    assert donor_letter.startswith('Dear {}:\n'.format('Peter Griffin'))


def test_donor_list():
    donors_list = list_of_donors()
    assert donors_list.startswith('DONORS: \n')
    assert len(donors_list.split('\n')) >= len(donors_db) + 3


def test_add_donation():
    record = add_donation('Daniel Castro', donors_db, -123)
    assert record['Daniel Castro'][-1] >= 0


def test_donor_in_db():
    record = add_donation('Daniel Castro', donors_db, -123)
    assert 'Charlie Brown' in record
