donor1 = ['Bobs Burger',400.50, 250.46]
donor2 = ['Peter Griffin', 865.23, 910.06, 454.25]
donor3 = ['Charlie Brown', 420.45, 250.67]
donor4 = ['Scooby Doo', 2000.60, 500.84]
donor5 = ['Luke Skywalker', 340.55, 67.89, 900.00]
donor_db = [donor1, donor2, donor3, donor4, donor5]

response = ['Peter Griffin']

for donor in donor_db:
    for item in donor:
        # while response[0] not in donor:
        if response[0] in item:
            print('True: {}'.format(response))
        elif response[0] not in item:
            print('"{}" not in database'.format(response[0]))
            print('Adding {} to donor_db'.format(response[0]))
            donor_db.append(response)
            break
print(donor_db)
