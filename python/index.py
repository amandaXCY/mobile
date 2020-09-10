from bs4 import BeautifulSoup
import os
import xlwt
import re
from openpyxl import Workbook
from lxml import etree


class BossData:
    def __init__(self):

        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('数据产品经理',cell_overwrite_ok=True)
        self.title = ('职位名称', '公司名称', '规模', '行业', '薪资', '年薪', '经验', '学历', '标签', '福利', 'job地址')
        self.coloumIndex = 1;
        self.detailUrls = []
        self.write_xlw(self.title, 0)
        self.open_file()


        if not os.path.exists('./dist/file'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs('./dist/file')

        self.workbook.save('./dist/file/job.xls')
        #self.workbook.save('./dist/file/job-back.xls')

    def open_file(self):
        path = './html'
        files = os.listdir(path);
        index = 0;
        for file in files:
            if file != ".DS_Store":

                if index > 0:
                    self.coloumIndex = self.coloumIndex + 29

                index = index + 1
                file = open(path + "/" + file)
                str_html = file.read()
                file.close()
                soup = BeautifulSoup(str_html, 'lxml')  # lxml为解析器
                self.parse_list2(soup)

    def parse_list2(self, soup):
        self.parse_job(soup)
        self.parse_company(soup)
        self.parse_scale(soup)
        self.parse_trades(soup)
        self.parse_salary(soup)
        self.parse_ee(soup)
        self.parse_tags(soup)
        self.parse_welfare(soup)
        self.parse_joburl(soup)

    def write_xlw(self, title, col):

        for i in range(len(title)):
            self.worksheet.write(col, i, title[i])

    def write_xlw_row(self, title, row,color ='black'):
        for i in range(len(title)):
            #self.worksheet.write(i+self.coloumIndex, row, title[i],xlwt.easyxf("font:colour_index %s;" % (color)) )
            self.worksheet.write(i + self.coloumIndex, row, title[i])

    # 职位名称
    def parse_job(self, soup):

        tags = []
        nodes = soup.find_all('span', {"class": 'job-name'})
        for node in nodes:

            tags.append(node.a.attrs['title'])

        self.write_xlw_row(tags, self.title.index('职位名称'))

    # 公司名称
    def parse_company(self,soup):

        tags = []
        nodes = soup.find_all('div', {"class":'company-text'})
        for node in nodes:
            tags.append(node.a.attrs['title'])

        self.write_xlw_row(tags, self.title.index('公司名称'))

    # 规模
    def parse_scale(self,soup):
        tags = []
        nodes = soup.find_all('div', {"class": 'company-text'})

        for node in nodes:
            pattern = re.compile(r'(\d+(.*))')  # 用于匹配至少一个数字

            m = re.split(pattern,node.get_text())
            tags.append(m[1])
        self.write_xlw_row(tags, self.title.index('规模'))

    # 行业
    def parse_trades(self,soup):
        tags = []
        nodes = soup.find_all('a', {"class": 'false-link'})
        for node in nodes:
            tags.append(node.get_text())
        self.write_xlw_row(tags, self.title.index('行业'))

    # 薪资
    def parse_salary(self,soup):
        tags = []
        year_salary = []
        nodes = soup.select('.job-limit > span.red')

        for node in nodes:

            text = node.get_text().split('·')
            tags.append(text[0])

            if len(text) == 2:
                year_salary.append(text[1])
            else:
                year_salary.append("")

        self.write_xlw_row(tags, self.title.index('薪资'))
        self.write_xlw_row(year_salary, self.title.index('年薪'))

    # 经验和学习Experience、Education
    def parse_ee(self,soup):
        experience = []
        education = []
        nodes = soup.select('.job-limit p')
        for node in nodes:
            contents = node.contents;

            contents_len = len(contents)
            if contents_len == 3:
                experience.append(contents[0]);
                education.append(contents[2]);

            elif contents_len == 2:
                if '年' in contents[0]:
                    experience.append(contents[0])
                    education.append("");
                elif '经验不限' in contents[0]:
                    experience.append(contents[0])
                    education.append("");
                else:
                    experience.append("");
                    education.append(contents[0])

        self.write_xlw_row(experience, self.title.index('经验'))
        self.write_xlw_row(education, self.title.index('学历'))

    def parse_tags(self, soup):

        tag_nodes = soup.select('.tags')

        tags = []
        for node in tag_nodes:
            tags.append(node.get_text()[1:].replace('\n','、'))

        self.write_xlw_row(tags, self.title.index('标签'))

    #job detali
    def parse_joburl(self, soup):
        nodes = soup.select('.job-name a')
        tags = []
        for node in nodes:
            link = 'https://www.zhipin.com' + node.attrs['href'];
            name ="详情"
            url = 'HYPERLINK("%s","%s")' % (link, name)

            tags.append(xlwt.Formula(url))
            self.detailUrls.append(link)


        self.write_xlw_row(tags, self.title.index('job地址'), 'blue')

    # 福利
    def parse_welfare(self,soup):
        tag_nodes = soup.select('.info-append .info-desc')
        tags = []
        for node in tag_nodes:
            tags.append(node.get_text())
        self.write_xlw_row(tags, self.title.index('福利'))

    # 福利
    def parse_welfare(self, soup):
        tag_nodes = soup.select('.info-append .info-desc')
        tags = []
        for node in tag_nodes:
            tags.append(node.get_text())


        self.write_xlw_row(tags, self.title.index('福利'))

BossData()
