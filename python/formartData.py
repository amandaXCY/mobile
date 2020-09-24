import numpy as np
import pandas as pd
from openpyxl import load_workbook
from python.variable import xlsx_path
import pandas as pd
from python.variable import xlsx_title
import xlrd

class Alysis:
    def __init__(self):
        self.red_file();
        self.read_row('职位名称')

    def red_file(self):
        wookhook = pd.read_excel(xlsx_path,sheet_name=[0],index_col=None, na_values=['NA'])
        self.sheet = wookhook[0]

    def read_row(self,name):
        data = list(self.sheet[name])
        data_set = set(data)

        print(len(data_set),data_set)





A

