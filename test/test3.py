#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import requests
commentURL='http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    comments=requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text)
    return jd['result']['count']['total']
#print(http://news.sina.com.cn/c/gat/2018-07-03/doc-ihevauxi7322609.shtml)