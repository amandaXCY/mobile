import pandas as pd



class test():
    def __init__(self):
        self.read_file()
        self.run_exce()

    def read_file(self):
        excel = pd.ExcelFile('dist/file/教育信息.xlsx')
        self.sheet = pd.read_excel(excel)

    def run_exce(self):

        self.sheet.fillna(method='pad',inplace=True)
        a = self.sheet.sort_values(by=['类别','发表期刊论文(求和)'],ascending=[True,True])
        print(a)




test()