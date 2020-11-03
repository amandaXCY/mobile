import pandas as pd
import os
from python.variable import save_path, xlsx_path, xlsx_title


def filter_unlink(df):
    return df[0].str.find('link') > -1

def filter_phoenix(df):
    return df['index'].str.find('@beisen-phoenix') > -1

class run:
    def __init__(self,saveFileName,include=[]):

        self.monorepo_path = os.path.abspath('../../../stnew03/ux-ocean-cmps-monorepo/src/components/')
        self.saveFileName = saveFileName;
        self.include = include
        self.coloums = ['from', 'index', 0]
        self.json_collection = pd.DataFrame(columns=self.coloums)
        self.read_file()
        self.save_file_skin()

    def read_file(self):
        area = self.include;
        if len(area) == 0:
            area = os.listdir(self.monorepo_path)
            self.include = area;
        self.read_component(area)
        self.read_link()
        self.read_link()
        self.read_link()


    def read_link(self):

        link_json = self.json_collection.loc[filter_unlink(self.json_collection), :].copy()
        link_json.loc[:, 'path'] = link_json[0].str.replace(r'link(.*)\/', '')
        components = list(link_json['path'])
        if len(components) == 0:
            return
        # 删除linkz
        self.json_collection.drop(axis=0, index=link_json.index,inplace=True)
        self.read_component(components,self.read_link)

    def read_component(self, components,callback=lambda x:x):
        path = self.monorepo_path

        for key in range(len(components)):
            item = components[key]
            components_path = os.path.join(path, item);
            if item.find('.') == 0:
                pass
            elif not os.path.exists(components_path):
                pass
            else:
                self.read_package(components_path, item)

        if type(callback) == 'function':
            callback()

    def read_package(self, path, name):

        package_path = os.path.join(path, 'package.json')
        json = pd.read_json(package_path, orient='index')

        if "dependencies" in json.index:
            dependencies = pd.read_json(json.loc['dependencies'].to_json())
            dependencies.reset_index(level=0, inplace=True)
            dependencies.loc[:, 'from'] = [name] * dependencies.shape[0]
            self.json_collection = self.json_collection.append(dependencies, ignore_index="True")

        if "devDependencies" in json.index:
            devDependencies = pd.read_json(json.loc['devDependencies'].to_json())
            devDependencies.reset_index(level=0, inplace=True)
            devDependencies.loc[:, 'from'] = [name] * devDependencies.shape[0]
            self.json_collection = self.json_collection.append(devDependencies, ignore_index="True")

    def save_file_skin(self):

        file_name = os.path.abspath(os.path.join(save_path,self.saveFileName))
        print(file_name)
        with pd.ExcelWriter(file_name) as excel:
            # 去掉link
            df2 = self.json_collection.copy()
            df2.to_excel(excel, sheet_name='all')

            # total from
            df4 = df2.copy()
            df4 = df4.drop_duplicates(subset=['from'],ignore_index=True)
            df4.to_excel(excel, sheet_name='from')

            # 仅beisen-phoenix
            df3 = self.json_collection.copy()
            filter_df3 = df3.loc[filter_phoenix(df3), :]
            filter_df3 = filter_df3.sort_values('index',ignore_index=True)
            filter_df3.to_excel(excel, sheet_name='phoenix')

            # 去重组件名
            df5 = filter_df3.copy().drop_duplicates(subset=['index'],ignore_index=True)
            df5.to_excel(excel, sheet_name='phoenix-unrepeat-index')

            df6 = filter_df3.copy().drop_duplicates(subset=['index',0],ignore_index=True)
            df6.to_excel(excel, sheet_name='phoenix-unrepeat-index-version')

            #组件
            df7 = pd.Series(self.include)
            df7.to_excel(excel, sheet_name='components')


            excel.save()




tms_bti = ['message', 'comfirm', 'filter',
                   'subscript-drawer', 'pagination',
                   'free-report-save-as-from', 'tablet-drill', 'loading',
                   'empty', 'breadcrumb', 'theme']
all =[]
run(saveFileName="ocean-monorepo.xlsx",include=all)
run(saveFileName="ocean-monorepo-bti.xlsx",include=tms_bti)
