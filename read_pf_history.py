__author__ = 'dimitrios'

import numpy as np
import pandas as pd
import os

def read_pf_history():
    history_file = os.sep.join([os.getcwd(),
                                'pffolder',
                                'data_history'])
    data = pd.read_html(history_file, header=0)[0]
    return data

# ddd = read_pf_history()
# print(ddd[pd.isnull(ddd['Wind & swell wave height(meters)'])]['Speed(knots)'])

def read_last_report():
    report_file = os.sep.join([os.getcwd(),
                               'pffolder',
                               'data_history'])
    data = pd.read_html(report_file, header=0)[0]
    return data

ddd = read_last_report()
ddd = ddd[[0, 2, 3, 4, 6, 7, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29]]
print(ddd.tail())