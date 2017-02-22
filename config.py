#!/usr/bin/env python

ttg_url = 'https://totheglory.im/'
mt_url = 'https://tp.m-team.cc/'
hdc_url = 'https://hdchina.club/'
chd_url = 'https://chdbits.co/'

ttg_passkey = 'test'
mt_passkey = 'test'
hdc_passkey = 'test'
chd_passkey = 'test'


mt_cookie = 'tp=MWYzZWI1OGRjYzNkOWRkZTkyNGZhN2MzMWEzYTRkOWZlY2I1M2MzMA%3D%3D'
ttg_cookie = 'PHPSESSID=55ubfavrhg2svpufn67jh57lj4; __cfduid=d780dd1595bcb0b626606e636b64abc211484618569; uid=128571; pass=5e02371e80f2b1068e258a4e71d9f94f; laccess=1487071374; __utmt=1; __utma=230798618.83627285.1480934139.1487123301.1487145342.104; __utmb=230798618.1.10.1487145342; __utmc=230798618; __utmz=230798618.1480934139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CNZZDATA4085974=cnzz_eid%3D9361471-1480932664-https%253A%252F%252Ftotheglory.im%252F%26ntime%3D1487142426; _ga=GA1.2.83627285.1480934139; _gat=1'
hdc_cookie = '__cfduid=d38ceb297978e307a9660fa148ea1ec701481074295; mv_secure_uid=Mjc5MjU2; mv_secure_pass=14490fe606886cef50a8263c323774bf; mv_secure_ssl=eWVhaA%3D%3D; mv_secure_tracker_ssl=eWVhaA%3D%3D; mv_secure_login=bm9wZQ%3D%3D; c_lang_folder=chs; __utmt=1; __utma=9389676.1474364046.1481074296.1487311276.1487383737.104; __utmb=9389676.5.10.1487383737; __utmc=9389676; __utmz=9389676.1481074296.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
chd_cookie = '__cfduid=dab2f9452bd70f817ea0d19b916f7c5511483072767; c_secure_uid=OTAxOQ%3D%3D; c_secure_pass=bad7acf59a93a64d36f1388a3d8fdda4; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'

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
