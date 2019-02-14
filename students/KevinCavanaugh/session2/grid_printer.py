def column(a):
    print("+", end=" ")
    for i in range(a-1):
        print("- - - - +", end=" ")
    print("- - - - +")


def rows(a):
    print("|", end=" ")
    for i in range(a-1):
        print("        |", end=" ")
    print("        |")


def grid_printer(a,b):
    column(a)
    for i in range(b):
        for i in range(4):
            rows(a)
        column(a)


a = int(input("columns: "))
b = int(input("rows: "))
grid_printer(a, b)
