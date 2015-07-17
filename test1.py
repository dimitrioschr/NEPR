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