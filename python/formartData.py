import numpy as np
import pandas as pd
from openpyxl import load_workbook
from python.variable import xlsx_path
import pandas as pd
import os
from python.variable import xlsx_title
import xlrd

class GenerateJSON:
    def __init__(self):

        self.red_file();
        self.read_row('经验','experience')

    def red_file(self):
        wookhook = pd.read_excel(xlsx_path, sheet_name=[0], index_col=None, na_values=['NA'])
        self.sheet = wookhook[0]

    def read_row(self, name,json_name):
        data = list(self.sheet[name])
        data_set = pd.Series(data)
        count = data_set.value_counts()

        self.write_in(count,json_name)

    def write_in(self,count,json_name):

        data_folder = os.path.abspath('../website/src/dist')
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

        content = count.to_json(data_folder + '/%s.json' % (json_name), orient='split', force_ascii=False)





GenerateJSON()



