
from python.variable import xlsx_path
import pandas as pd
import os

class GenerateJSON:
    def __init__(self):

        self.red_file();
        self.read_row('经验','experience')
        self.read_row('学历', 'education')

    def red_file(self):
        wookhook = pd.read_excel(xlsx_path, sheet_name=[0], index_col=None, na_values=['NA'])
        self.sheet = wookhook[0]
        self.sheet = self.sheet.convert_dtypes()

        a = self.sheet.query('经验 == "1-3年"')['薪资']
        #self.sheet = self.sheet.assign(经验2 = lambda x: x['经验'],经验薪资 = lambda x: x['经验'] +x['薪资'])
        self.sheet['经验3'] = ""
        self.sheet.loc[self.sheet['经验']== '1-3年','经验3'] = '对'
        self.sheet.loc[self.sheet['经验'] != '1-3年', '经验3'] = '错'
        print(self.sheet['经验'].describe())
        print(self.sheet['经验'].value_counts())




        # print(self.sheet._stat_axis.values)
        # print(a.loc[:, ['经验', '薪资']])


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



