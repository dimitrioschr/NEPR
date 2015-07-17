__author__ = 'operation3'

import pandas as pd
import numpy as np
import xlrd
import sqlite3
import os


pfdbconn = sqlite3.connect(os.sep.join([os.getcwd(), 'databases', 'pfdb.db']))
pfdbconn.commit()
pfdbconn.close()

vsldbconn = sqlite3.connect(os.sep.join([os.getcwd(), 'databases', 'vsldb.db']))
vsldbconn.commit()
vsldbconn.close()

filename = os.sep.join([os.getcwd(),
                        'vslfolder',
                        'NEPR PHOENIX RISING',
                        'NEPR PHOENIX_RISING (1B2015) Chiba-Long Beach.xlsx'])
print(filename)
book = xlrd.open_workbook(filename)
sheet = book.sheet_by_index(0)
print(sheet.col(1)[2])

neprfolders = os.listdir(os.sep.join([os.getcwd(), 'vslfolder']))
print(neprfolders)
