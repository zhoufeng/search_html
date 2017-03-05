#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
import time



def s(int):
    time.sleep(int)
class Mobile1688CateParse:

    def __init__(self):
        #self.browser = webdriver.PhantomJS();
        self.browser = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
    '''
    登陆
    '''
    def login(self):
        url="https://login.m.taobao.com/login.htm?loginFrom=wap1688&redirectURL=http%3A%2F%2Fm.1688.com%2Fpass.html%3Fdone%3Dhttp%253A%252F%252Fm.1688.com"
        browser = self.browser
        browser.get(url)
        browser.find_element_by_id('username').send_keys(u'kongjishisecom')
        browser.find_element_by_id('password').send_keys(u'796685zai')
        browser.find_element_by_id('submit-btn').click()

    '''
    根据公司名称查询memberId
    '''
    def searchMemberId(self,companyName):
        url="http://m.1688.com/page/search.html?type=company&keywords=%s"%(companyName)
        browser = self.browser
        browser.get(url)
        time.sleep(1)
        print browser.page_source

    def searchCategory(self,memberId):
        url="http://winport.m.1688.com/page/category.html?spm=a26g8.7664812.0.0.HsNOjq&memberId=%s"%(memberId)
        browser = self.browser
        browser.get(url)
        print browser.page_source

    '''
    解析url
    '''
    def parse(self,url):
        browser = self.browser
        browser.get(url)
        print browser.page_source
        #browser.quit()



if "__main__"==__name__:
    m = Mobile1688CateParse()
    #for i in range(0,1):
    #m.parse("http://m.1688.com/page/offerlist.html?catId=80185896&catPid=78573644&isUserDefined=true&title=9%E6%9C%884%E5%8F%B7%E6%96%B0%E6%AC%BE&memberId=b2b-2854844521fed59")
    #m.login()
    #m.searchMemberId("韩版童装")
    m.searchCategory("b2b-2854844521fed59")
    "http://m.1688.com/gongsi_search/-B9ABD7D0.html"