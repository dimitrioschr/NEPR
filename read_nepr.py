
import xlrd
import pandas as pd
from pandas import DataFrame


# utility functions
read_column = lambda n, m, s: sheet.col_values(n, m, m + s)
# read column n, starting from cell in row m, slice length s, and return a list
convert_to_date = lambda l: list(map(lambda d: xlrd.xldate_as_tuple(d, 0), l))
# convert list of Excel dates into python datetime tuple
trim = lambda l: list(map(lambda e: e.replace('0', '', 1) if e.startswith('0') else e, l))
# trim leading zeros from a list of coordinates strings
count_floats = lambda l: sum(map(lambda x: 1 if type(x) == float else 0, l))
# count number of floats in a list
def df_from_sheet(sheet, basecol_number, columns_to_read, datetime_columns, trim_columns, start_row):
    n_act_rows = sheet.nrows
    basecol = sheet.col_values(basecol_number, start_row, n_act_rows)
    n_act_rows = count_floats(basecol)
    data = []
    for c in columns_to_read:
        if c in datetime_columns:
            data.append(convert_to_date(read_column(c, start_row, n_act_rows)))
        elif c in trim_columns:
            data.append(trim(read_column(c, start_row, n_act_rows)))
        else:
            data.append(read_column(c, start_row, n_act_rows))
    return DataFrame(data).T
# get a Dataframe from a specified sheet


book = xlrd.open_workbook('test.xlsx')

# process sheet 'Noon Position'
sheet = book.sheet_by_index(2)
basecol_number = 0
columns_to_read = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 22]
datetime_columns = [0, 1, 2]
trim_columns = [3, 4]
start_row = 8
# data start from row 8

df1 = df_from_sheet(sheet, basecol_number, columns_to_read, datetime_columns, trim_columns, start_row)
print(df1)


# process sheet 'Weather Condition'
sheet = book.sheet_by_index(3)
basecol_number = 3
columns_to_read = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 22]
datetime_columns = [3, 4]
trim_columns = []
start_row = 2
# data start from row 2

df2 = df_from_sheet(sheet, basecol_number, columns_to_read, datetime_columns, trim_columns, start_row)
print(df2)


# process sheet 'Bunkers and Lubs'
sheet = book.sheet_by_index(4)
basecol_number = 0
columns_to_read = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 26]
datetime_columns = [0, 1]
trim_columns = []
start_row = 2
# data start from row 2


df3 = df_from_sheet(sheet, basecol_number, columns_to_read, datetime_columns, trim_columns, start_row)
print(df3)

# process sheet 'Environmental'
sheet = book.sheet_by_index(5)
basecol_number = 0
columns_to_read = [0, 1, 3, 4, 5, 7, 8, 9, 10, 12]
datetime_columns = [0, 1]
trim_columns = []
start_row = 5
# data start from row 5


df4 = df_from_sheet(sheet, basecol_number, columns_to_read, datetime_columns, trim_columns, start_row)
print(df4)


res = df1.merge(df2, on=[0, 1]).merge(df3, on=[0, 1]).merge(df4, on=[0, 1])
