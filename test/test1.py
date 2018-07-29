#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from test3 import getCommentCounts
def GetNewsDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    res.encoding='utf8'                         #编码方式为utf8
    soup=BeautifulSoup(res.text,'html.parser')
    result['title']=soup.select('.main-title')[0].text           #抓取标题
    timesource=soup.select('.date-source')[0].contents[1].text      #抓取时间
    result['dt']=datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')  #从字符串改变时间格式
    if len(soup.select('.date-source a'))>0:
        result['source'] = soup.select('.date-source a')[0].text  # 抓取来源
    else:
        result['source'] = 0
    result['article']=' '.join([p.text.strip() for p in soup.select('#article p')])
    result['editor']=soup.select('.show_author')[0].text.strip('责任编辑：') #strip(移除指定字符) 抓取编辑名字
    result['comments']=getCommentCounts(newsurl)
    return result
#print(GetNewsDetail('http://news.sina.com.cn/c/gat/2018-07-03/doc-ihevauxi7322609.shtml'))
#print(GetNewsDetail('http://news.sina.com.cn/c/nd/2018-07-25/doc-ihfvkitw5286754.shtml'))
