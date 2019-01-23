# Title: Series
# Change Log: (Who,When,What)
# dcastrowa, 01-2019-19, created file

# -----Data----- #


numbers = list(range(8))

# ------Processing----- #


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n2=0, n3=1):
    if n == 0:
        return n2
    elif n == 1:
        return n3
    else:
        return sum_series(n - 1, n2, n3) + sum_series(n - 2, n2, n3)


# -----Presentation----- #


for number in numbers:
    answer = fibonacci(number)
    print(answer)
print()
for number in numbers:
    answer = lucas(number)
    print(answer)
print()
for number in numbers:
    answer = sum_series(number)
    print(answer)


