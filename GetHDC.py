#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re
import requests
import time
import sqlite3
import config

url = config.hdc_url
headers = config.hdc_headers
passkey = config.hdc_passkey
t_url = url + 'torrents.php'

def showtop():
    conn = sqlite3.connect('pttop.db')
    conn.text_factory = str
    cur = conn.cursor()
    site = 'HDC'
    s = requests.Session()
    s.headers.update(headers)
    r = s.get(t_url)
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable = soup.find("table",{"class" : "torrent_list"})
    for row in fulltable.find_all("tr",class_=["stickz_bg","sticky_bg"],recursive=False):
        torrent_fix = row.find("td",{"class":"t_name"}).find("tr").find_all("td")[1]
        torrent_misc = torrent_fix.h3.a
        title = torrent_misc['title']
        size = row.find("td",{"class":"t_size"}).text
        site_id = re.search(r'\d+(?=&)',torrent_misc['href']).group()
        up_time = row.find("td",{"class":"t_time"}).span['title']
        upltime = int(time.mktime(time.strptime(up_time,"%Y-%m-%d %H:%M:%S")))
        try:
            name = torrent_fix.h4.text
        except:
            name = ''
        t_link = url + "details.php?id=" + site_id + "&hit=1"
        d_link = url + "download.php?id="+ site_id + "&passkey=" + passkey
        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()
    conn.close()

if __name__ == '__main__':
    showtop()
