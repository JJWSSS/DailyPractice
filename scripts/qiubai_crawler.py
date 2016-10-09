import requests
from bs4 import BeautifulSoup
import os
import time
from multiprocessing import Pool
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        func(*args, **kwargs)
        print(time.clock() - start_time)
    return wrapper


class QiubaiCrawler(object):
    def __init__(self, page_number, base_url, base_path):
        self.base_url = base_url
        self.page_number = page_number
        self.base_path = base_path
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def crawler(self, i):
        path = os.path.join(self.base_path, str(i))
        if not os.path.isdir(path):
            os.mkdir(path)
        response = requests.get(self.base_url+str(i)+'.html', headers=self.headers)
        print(i, response.status_code)
        soup = BeautifulSoup(response.text, 'html5lib')
        divs = soup.find_all('div', class_='ui-module')
        for num, div in enumerate(divs):
            if div.find('div', style='text-align: center;'):
                filename = (div.find('div', style='text-align: center;')).a.img['alt'].encode('ISO-8859-1').decode('gbk', 'ignore')
                src = div.find('div', style='text-align: center;').a.img['src']
                self.download_photo(src, path, filename)

    def download_photo(self, src, path, filename):
        response = requests.get(src, headers=self.headers)
        if src.split('.')[-1] == 'gif':
            with open(os.path.join(path, (filename + '.gif')), 'wb') as f:
                f.write(response.content)
        else:
            with open(os.path.join(path, (filename + '.jpg')), 'wb') as f:
                f.write(response.content)

    @measure_time
    def start(self):
        if not os.path.isdir(self.base_path):
            os.mkdir(self.base_path)
        p = Pool(10)
        for i in range(1, self.page_number + 1):
            p.apply_async(self.crawler, args=(i,))
        p.close()
        p.join()


if __name__ == '__main__':
    qiubai = QiubaiCrawler(538, 'http://www.qiubaichengren.com/', '/Users/JJW/Downloads/qiubai_picture')
    qiubai.start()


