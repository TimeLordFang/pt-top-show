#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re
import requests
import time
import sqlite3
import config

url = config.ttg_url
headers = config.ttg_headers
passkey = config.ttg_passkey
t_url = url + "browse.php?c=M"

def showtop():
    conn = sqlite3.connect('pttop.db')
    conn.text_factory = str
    cur = conn.cursor()
    s = requests.Session()
    s.headers.update(headers)
    r = s.get(t_url)
    site = 'TTG'
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable =  soup.find("table",{"id" : "torrent_table"})
    for row in fulltable.find_all("tr",class_=["hover_hr  sticky","hover_hr"],recursive=False):
        site_id = row["id"]
        up_time = row.find_all("td",{"align":"center"})[1].text
        #upl_time = int(time.mktime(time.strptime(up_time,"%Y-%m-%d%H:%M:%S")))
        upltime = time.strftime("%Y-%m-%d %H:%M:%S", (time.strptime(up_time,"%Y-%m-%d%H:%M:%S")))
        time.strftime("%Y-%m-%d %H:%M:%S",)
        size = row.find_all("td",{"align":"center"})[3].text
        torrent_fix = str(row.find("td",{"align":"left"}).find("div").a.b)
        #title = re.split('<|>',torrent_fix)[2] #原盘DIY制作者@字符使用了邮件保护js，直接舍弃处理
        title_x = re.sub(r'</?\w+[^>]*>','',torrent_fix.split('<br/>')[0]).strip()
        title = re.split(r"\[",title_x)[0]
        try:
            name = re.sub(r'</?\w+[^>]*>','',torrent_fix.split('<br/>')[1]).strip()
        except:
            name = ''

        t_link = url + "t/" + site_id + "/"
        d_link = url + "dl/" + site_id + "/" + passkey
        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()
    conn.close()

if __name__ == '__main__':
    showtop()
