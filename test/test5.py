#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import pymysql

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
for i in range(1,30):
    newsurl=url.format(i)
    newsary=parseListLinks(newsurl)
    news_total.extend(newsary)


# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='0511',
    database='test',
    charset='utf8'
)

for i in range(len(news_total)):
    cursor = connect.cursor()
    sql = "INSERT INTO test (  article, comments,dt,editor,source,title) VALUES (  '%s', %d,'%s','%s','%s','%s' )"
    data = ( news_total[i]['article'], news_total[i]['comments'],news_total[i]['dt'],news_total[i]['editor'], news_total[i]['source'],news_total[i]['title'])
    cursor.execute(sql % data)
    connect.commit()
print('成功插入', cursor.rowcount, '条数据')
# 关闭连接
cursor.close()
connect.close()