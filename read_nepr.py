
import xlrd
import pandas as pd
from pandas import DataFrame


# utility functions
read_column = lambda n, m: sheet.col_values(n, m, m + n_act_rows)
# read column n, starting from cell in row m and return a list
convert_to_date = lambda l: list(map(lambda d: xlrd.xldate_as_tuple(d, 0), l))
# convert list of Excel dates into python datetime tuple
trim = lambda l: list(map(lambda e: e.replace('0', '', 1) if e.startswith('0') else e, l))
# trim leading zeros from a list of coordinates strings
count_floats = lambda l: sum(map(lambda x: 1 if type(x) == float else 0, l))
# count number of floats in a list


book = xlrd.open_workbook('test.xlsx')

# process sheet 'Noon Position'
sheet = book.sheet_by_index(2)
start_row = 8
# data start from row 8
n_act_rows = sheet.nrows
basecol = sheet.col_values(0, start_row, n_act_rows)
n_act_rows = count_floats(basecol)

columns_to_read = list(range(7)) + list(range(8, 14)) + [22]
data = []
for c in columns_to_read:
    if c in [0, 1, 2]:
        data.append(convert_to_date(read_column(c, start_row)))
    elif c in [3, 4]:
        data.append(trim(read_column(c, start_row)))
    else:
        data.append(read_column(c, start_row))

df = DataFrame(data).T
print(df)


# process sheet 'Weather Condition'
sheet = book.sheet_by_index(3)
start_row = 2
# data start from row 2
n_act_rows = sheet.nrows
basecol = sheet.col_values(3, start_row, n_act_rows)
n_act_rows = count_floats(basecol)

columns_to_read = list(range(3, 17)) + [22]
data = []
for c in columns_to_read:
    if c in [3, 4]:
        data.append(convert_to_date(read_column(c, start_row)))
    else:
        data.append(read_column(c, start_row))

df = DataFrame(data).T
print(df)


# process sheet 'Bunkers and Lubs'
sheet = book.sheet_by_index(4)
start_row = 2
# data start from row 2
n_act_rows = sheet.nrows
basecol = sheet.col_values(0, start_row, n_act_rows)
n_act_rows = count_floats(basecol)

columns_to_read = list(range(12)) + [26]
data = []
for c in columns_to_read:
    if c in [0, 1]:
        data.append(convert_to_date(read_column(c, start_row)))
    else:
        data.append(read_column(c, start_row))

df = DataFrame(data).T
print(df)


# process sheet 'Environmental'
sheet = book.sheet_by_index(5)
start_row = 5
# data start from row 5
n_act_rows = sheet.nrows
basecol = sheet.col_values(0, start_row, n_act_rows)
n_act_rows = count_floats(basecol)

columns_to_read = list(range(13))
columns_to_read.remove(2)
columns_to_read.remove(6)
columns_to_read.remove(11)
print(columns_to_read)
data = []
for c in columns_to_read:
    if c in [0, 1]:
        data.append(convert_to_date(read_column(c, start_row)))
    else:
        data.append(read_column(c, start_row))

df = DataFrame(data).T
print(df)

