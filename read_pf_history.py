__author__ = 'dimitrios'

import pandas as pd
import os

def read_pf_history():
    history_file = os.sep.join([os.getcwd(),
                                'pffolder',
                                'data_history'])
    data = pd.read_html(history_file, header=0)[0]
    return data

print(read_pf_history().head())