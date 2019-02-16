from mailroom_part4B import list_of_donors
from mailroom_part4B import add_donation

donors_db = {'Bob Belcher': (400.50, 250.46),
             'Peter Griffin': (865.23, 910.06, 454.25),
             'Charlie Brown': (420.45, 250.67),
             'Scooby Doo': (2000.60, 500.84),
             'Luke Skywalker': (340.55, 67.89, 900.00)}


def test_donor_list():
    donors_list = list_of_donors()
    assert donors_list.startswith('DONORS: \n')
    assert len(donors_list.split('\n')) >= len(donors_db) + 3


def test_add_donation():
    record = add_donation('Daniel Castro', donors_db, -123)
    assert record['Daniel Castro'][-1] >= 0




