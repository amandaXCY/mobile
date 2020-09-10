
import requests
import time
import random
import math
import os
from bs4 import BeautifulSoup


urls = ["https://www.zhipin.com/job_detail/0d3e5eff1e470d7a33V709y6GFU~.html"]

headers = {
    'cookie': 'lastCity=101010100; _bl_uid=h6kz0e03l2sn3yiL558y343mgvqR; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1599066703,1599066721,1599142895,1599573879; __g=-; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1599573926; __c=1599573879; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F8dec759c9261d5f13nB93dW_GFc~.html&r=&g=&friend_source=0&friend_source=0; __a=22275949.1596343816.1599142896.1599573879.271.6.5.242; __zp_stoken__=67f6bC0VGf09pEV1CLXZ5bjduTwccZW1gEihTY05CYzslPkp8Rm8FT0IjUCgwN2g1Wjs6Ewgwb3MCOUEaUUlwR1c2H1IeQUBUBV0Dbg9ZDGIHGD0rLksVXH8gShJlPg1HXGpHdUxOdVt2PAl5JQ%3D%3D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    # ':authority': 'www.zhipin.com',
    # ":method": ' GET',
    # ":path:": url,
    # ":scheme:": 'https',
}
proxy ={
    'http': 'http://110.243.26.4:9999',
    #'https': 'https://117.85.105.170:808'
}
startTime = 0
tag = 0;


for index in range(len(urls)):
    url = urls[index]
    sleep_time = startTime + math.ceil(random.uniform(1,1))
    print(sleep_time)
    time.sleep(int(sleep_time))

    r = requests.get(url, headers=headers, proxies=proxy,stream=True)
    time.sleep(int(sleep_time))
    url_query = url.split('/')
    file_name = url_query[-1]


    if('.' in file_name):
        file_name = url_query[-1].split('.')[0]
    
    path = './boss/dist/detail-html/'
    file_name = path + '%s.html' % (file_name)
    folder = os.path.exists(path)

    # 创建文件夹
    if not folder:
        os.makedirs(path)

    else: 
        with open(file_name,'w+') as fd:
            fd.write(str(r.text))
            soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
            job_intro = soup.select('.job-sec')
            print(job_intro)
           