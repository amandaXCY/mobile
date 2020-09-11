import os
from os import path

xlsx_title = ('职位名称', '公司名称', '规模', '行业', '薪资', '年薪', '经验', '学历', '标签', '福利', 'job地址')
xlsx_name = 'job.xlsx'
# 当前文件的路径
current_file_path = path.abspath(path.dirname(__file__))

#保存文件的路径
save_path = path.abspath(path.join(current_file_path,'./dist/file'))


#计算得到excel路径
xlsx_path = path.abspath(path.join(current_file_path,save_path,xlsx_name))

