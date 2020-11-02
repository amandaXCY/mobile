from bs4 import BeautifulSoup
import os
import tomd
import re
import shutil
import time
import random


class HTML2Md:
    def __init__(self, path, contetClasName):
        self.root = '/Users/amanda/Documents/mweb/mweb/collect-web/'
        self.root = '/Users/amanda/Downloads/mweb'

        self.name = self.file_name(path)[0]
        self.path = self.file_name(path)[1]

        folder_name = time.strftime("%Y%m%d", time.localtime())
        self.dist_folder = self.generatePath("./{0}".format(folder_name))
        self.dist_media = self.generatePath("./{0}/media".format(folder_name))

        str_html = self.read_file(path)

        soup = BeautifulSoup(str_html, 'lxml')  # lxml为解析器
        content = str(soup.select(contetClasName)[0])



        # to markdown
        markdown_content = tomd.Tomd(content).markdown
        print(markdown_content)
        self.cleanHTMLTargert(markdown_content)

    def file_name(self, path):
        name = path.split('/')[-1].split('.')[-2]
        src = path.split('/')[:-1]
        return (name,'/'.join(src))

    def read_file(self, path):
        file = open(path)
        str_html = file.read()
        file.close()
        return str_html

    def new_folder(self,name):
        if not os.path.exists(name):
            os.mkdir(name)

    def cleanHTMLTargert(self, content):

        array_content = content.split('\n')
        file_name = ""
        new_content = []

        self.new_folder(self.dist_folder)
        self.new_folder(self.dist_media)

        for item in array_content:

            if item.strip() != "":
                if file_name == "":
                    file_name = item.replace('#',"").strip()


            # 去除多余的标签
            pattern = re.compile(r'(<\/?(h2|br|font)\/?>)')
            item = re.sub(pattern, "", item)

            # image多余的标签
            soup = BeautifulSoup(item, 'lxml')  # lxml为解析器
            image = soup.select('img')

            if len(image) > 0:

                image_src = image[0].attrs['src']
                image_type = ".jpg";

                if image_src.rfind('.') > 0:
                    image_type = image_src[image_src.rfind('.'):]

                abs_src = os.path.join(self.path, image_src)
                abs_src = os.path.abspath(abs_src)

                now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
                image_name = str(now_time) + str(random.randint(100, 200))
                copy_image_name = str(image_name) + image_type
                shutil.copyfile(abs_src, "%s/%s" % (self.dist_media, copy_image_name))

                media = "![](./media/%s)" % (copy_image_name)
                item = re.sub(r"(<img .*>)", media, item)

            new_content.append(item)

        self.create_file('\n'.join(new_content), file_name)

    def generatePath(self,dist):
        path = os.path.join(self.root, dist)
        return os.path.abspath(path)

    def create_file(self, content,file_name):

        if not os.path.exists(self.dist_folder):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(self.dist_folder)

        file = open(self.dist_folder + '/' + file_name + '.md', 'w+')

        file.write(content)


a = HTML2Md("/Users/amanda/Downloads/dd.htm", '.ant-layout-content');
