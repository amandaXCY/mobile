from openpyxl import Workbook,load_workbook,utils,comments
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
import pandas as pd
import numpy as np

path ='/Users/amanda/Downloads/operator.xlsx'

class read_excel:
    def __init__(self):
        xlsx = pd.ExcelFile(path)
        self.sheet = pd.read_excel(xlsx, sheet_name="all",index_col=0)


        # df= workbook.drop(labels=[0,2])
        # workbook = pd.read_excel(path,sheet_name=1)
        # workbook.ax
        # .set_index('value',inplace=True)

        self.sheet = self.sheet.groupby(by=['tag','value']).sum()
        print(self.sheet)

    def run(self):

        #self.sheet.set_index(['name', 'value','component','group','dd'], drop=False)

        headerKey = list(self.sheet.columns)

        #df = pd.DataFrame([["插入指定的行"] * len(headerKey)],columns=headerKey)
        #self.sheet = self.sheet.append(df,ignore_index=True)


        self.sheet.to_excel('dd.xlsx')
        # for name,group in self.sheet:
        #     print(name)

        #df1 = self.sheet.loc[0:1]
        # df2 = self.sheet.loc[2:]
        # self.sheet = df1.append(df, ignore_index=True).append(df2, ignore_index=True)
        #
        # self.sheet.insert(loc=1,value=1,column='ddd')




read_excel()




