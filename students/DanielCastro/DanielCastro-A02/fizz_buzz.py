# Title: FizzBuzz
# Change Log: (Who,When,What)
# dcastrowa, 01-20190-19, created file


# ----------- Data ------------ #


numbers = list(range(1, 100))


# --------- Processing --------- #


def fizz_buzz(num):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

# ----- Presentation ----- #


for number in numbers:
    fizz_buzz(number)
