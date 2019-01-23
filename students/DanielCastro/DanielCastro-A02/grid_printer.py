# Title: FizzBuzz
# Change Log: (Who,When,What)
# dcastrowa, 01-20190-19, created file


# ----------- Data ------------ #


plus = '+ '
dash = '- '
space = '  '
col = '| '

# --------- Processing --------- #


def print_grid(n):
    multi_dash = dash * n
    line = plus + multi_dash
    full_line = line * 2 + plus
    column_lines = col + space * n
    full_col_line = column_lines * 2 + '|'
    print(full_line)
    print((full_col_line + '\n') * n, end=full_line)
    print('\n' + (full_col_line + '\n') * n, end=full_line)
    print()


def print_grid2(n, n2):
    multi_dash = dash * n2
    line = plus + multi_dash
    full_line = (line * n) + '+'
    column_lines = col + space * n2
    full_col_line = column_lines * n + '|'
    full_row = (full_col_line + '\n') * n2
    all_boxes = full_line + '\n' + full_row
    print(all_boxes * n, end=full_line)

# ----- Presentation ----- #


print_grid(3)
print_grid2(4, 3)
