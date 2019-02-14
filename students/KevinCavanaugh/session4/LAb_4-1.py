# Data
dict_row_1 = {'ID': 1, 'Name': 'Bob Smith', 'Email': 'Bsmith@Hotmail.com'}
dict_row_2 = {'ID': 2, 'Name': 'Sue Jones', 'Email': 'SueJ@yahoo'}
lst_table = [dict_row_1, dict_row_2]


# Processing
def add_stuff(my_list):
    new_dict_row += {'ID': {input('ID:')}, 'Name': {input('Name:')}, 'Email': {input('Email:')}}
    my_list += [new_dict_row]

add_stuff(lst_table)


# Presentation
print("ID|NAME|EMAIL")
for row in lst_table:
    print(row["ID"], row["Name"], row["Email"], sep='|')




