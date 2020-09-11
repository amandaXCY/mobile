import numpy as np
import pandas as pd
from openpyxl import load_workbook
from python.variable import xlsx_path
import pandas as pd
import xlrd

class Alysis:
    def __init__(self):
        self.red_file();

    def red_file(self):
        nyse = pd.read_excel(xlsx_path,sheet_name=[0],index_col=None, na_values=['NA'])
        s = nyse[0]
        title = list(s)
        s2 = nyse.copy()
        #print(s[title[0]])
        print(s.info())



Alysis()

