#!/usr/bin/python
#-*- coding: UTF-8 -*- 

import sqlite3
import os 

try:
    os.remove('pttop.db')
except:
    print("no pttop.db")
conn = sqlite3.connect('pttop.db')
conn.text_factory = str
print("Opened database successfully")

conn.execute('''CREATE TABLE PTTOP
       (ID integer PRIMARY KEY autoincrement,
	SITE	TEXT	NOT NULL,
	TITLE	TEXT	NOT NULL,
        NAME    TEXT,
	SITE_ID INT	NOT NULL,
        SIZE    CHAR(50)     NOT NULL,
	T_LINK	TEXT	NOT NULL,
	D_LINK	TEXT	NOT NULL,
	UPLTIME	INT	NOT NULL);''')
conn.close()
