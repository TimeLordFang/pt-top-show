#!/usr/bin/env python 

from bs4 import BeautifulSoup
import re
import requests
import time
import sqlite3
import config

url = config.mt_url
headers = config.mt_headers
passkey = config.mt_passkey
t_url = url + 'torrents.php'

def showtop():
    s = requests.Session()
    s.headers.update(headers)
    r = s.get(t_url)
    conn = sqlite3.connect('pttop.db')
    conn.text_factory = str
    cur = conn.cursor()
    soup =  BeautifulSoup(r.content, "lxml")
    fulltable = soup.find("table",{"class" : "torrents"})
    site = 'MT'
    for row in fulltable.find_all("tr",class_=['sticky_top','sticky_normal'],recursive=False):
        torrent_other = row.find_all("td",{"class":"rowfollow"})
        size = torrent_other[3].text
        up_time = torrent_other[2].span['title']
        upltime = int(time.mktime(time.strptime(up_time,"%Y-%m-%d %H:%M:%S")))
        torrent_table = row.find("table",{"class":"torrentname"})
        torrent_img = torrent_table.find("td",{"class":"torrentimg"}).a.find("img")['src']
        torrent_fix = torrent_table.find("td",{"class":"embedded"})
       	t_title = torrent_fix.a['title']
       	try:
       	    name = torrent_fix.find('br').nextSibling
       	except:
       	    name = ''
       	site_id = re.search(r'\d+(?=&)', torrent_fix.a['href'] ).group()

        t_link = url + "details.php?id=" + site_id + "&hit=1"
        d_link = url + "download.php?id=" +site_id + "&passkey=" + passkey + "&https=1"
        cur.execute("INSERT INTO PTTOP (SITE,TITLE,NAME,SITE_ID,SIZE,T_LINK,D_LINK,UPLTIME ) VALUES (?,?,?,?,?,?,?,?) " ,  (site,t_title,name,site_id,size,t_link,d_link,upltime))
        conn.commit()
    conn.close()

if __name__ == '__main__':
    showtop()
