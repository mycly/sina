#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import pandas
import pymysql
import datetime
from test1 import GetNewsDetail
def parseListLinks(url):
    newsdetails=[]
    res=requests.get(url)
    jd=json.loads(res.text)
    for ent in jd['result']['data']:
        newsdetails.append(GetNewsDetail(ent['url']))
    return newsdetails
#print(parseListLinks('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=1'))
url='http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}'
news_total=[]
for i in range(1,3):
    newsurl=url.format(i)
    newsary=parseListLinks(newsurl)
    news_total.extend(newsary)
print(news_total[0])
#df=pandas.DataFrame(news_total)
#df.to_excel('news729.xlsx')
