from bs4 import BeautifulSoup
from selenium import webdriver

class Notice():
    #driver = webdriver.Chrome('/Users/user/Desktop/pythonEx/chromedriver_win32/chromedriver')
    #C:\Users\user\Desktop\pythonEx\ApplyProjectRoomBot\phantomjs-2.1.1-windows\bin
    driver = webdriver.PhantomJS('../phantomjs-2.1.1-windows/bin/phantomjs')
    base_url = "http://sw.skhu.ac.kr/notice.brd?shell=/index.shell:268"

    def getNewNotice(self):
        self.driver.get(self.base_url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        new_notice = soup.select('table.table4list > tbody > tr:nth-of-type(2) > td:nth-of-type(2) > a')
        return new_notice[0]

    def simplify(self, result):
        title = result.text
        url = result.get('href')
        content = result.get('title')
        d = {'title': title, 'url': url, 'content': content}
        return d


n = Notice()
nn = n.getNewNotice()
print(n.simplify(nn))
