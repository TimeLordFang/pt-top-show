#!/usr/bin/env python

ttg_url = 'https://totheglory.im/'
mt_url = 'https://tp.m-team.cc/'
hdc_url = 'https://hdchina.club/'
chd_url = 'https://chdbits.co/'

ttg_passkey = 'test'
mt_passkey = 'test'
hdc_passkey = 'test'
chd_passkey = 'test'


mt_cookie = ''
ttg_cookie = ''
hdc_cookie = ''
chd_cookie = ''

comm_headers = {
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive'
    }

ttg_headers = comm_headers.copy()
ttg_headers.update({'Referer':ttg_url,'Cookie':ttg_cookie})
mt_headers = comm_headers.copy()
mt_headers.update({'Referer':mt_url,'Cookie':mt_cookie})
hdc_headers = comm_headers.copy()
hdc_headers.update({'Referer':hdc_url,'Cookie':hdc_cookie,'authority':'hdchina.club'})
chd_headers = comm_headers.copy()
chd_headers.update({'Referer':chd_url,'Cookie':chd_cookie,'authority':'chdbits.co'})
