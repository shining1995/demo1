# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from demo1.items import Demo1Item

class MydomainSpider(scrapy.Spider):
    name = 'joke'

    # 这个不是必须的；但是在某写情况下需要用得到，
    # 比如使用爬取规则的时候就需要了；它的作用是
    # 只会跟进存在于allowed_domains中的URL。
    # 不存在的URL会被忽略。
    # allow domains是一个数组，start_URL是一个字符串
    # allowed_domains = ['http://www.23wx.cc/']

    bash_url = 'http://www.23wx.cc/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23wx.cc/quanben/1', callback=self.parse)


    def parse(self, response):
        # print (response.text)
        max_num=1
        bashurl=str(response.url)[:-7]
        for num in range(1,int(max_num)+1):
            url=bashurl+'_'+str(num)+self.bashurl
            yield Request(url,callback=self.get_name)

    def get_name(self,response):
        tds=BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
        for td in tds:
            novelname=td.find('a').get_text()
            novelurl =td.find('a')['href']
            yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})
    # 这个return的item就是定义的item
    def get_chapterurl(self,response):
        item = Demo1Item()
        item['name']=str(response.meta['name']).replace('\xa0','')
        item['novelurl']=response.meta['url']
        category=BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
        auther=BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
        bash_url=BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')
        name_id=str(bash_url)[-6:-1].replace('/','')
        item['category']=str(category).replace('/','')
        item['author']=str(auther).replace('/','')
        item['name_id']=name_id
        yield item
        # return item
