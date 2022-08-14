import os,sys, re, requests, json, time
from time import sleep
from bs4 import BeautifulSoup as bs
from colorama import Fore
import json, re, sys,os
import time, hashlib, subprocess
from time import sleep                                    
try:
    import requests
    import colorama
    import bs4
    from datetime import datetime
except:
    print("Đang cài thư viện")
    os.system("pip install requests")
    os.system("pip install datetime")
    os.system("pip install colorama")
    os.system("pip install bs4")
    import requests
    from datetime import datetime
    import json,requests,time

from time import strftime
ngay=int(strftime('%d'))
key=str(ngay*192+1924)
print (key)
url=f'https://thaihao.online/keytoolfree.php?key={key}'
api_token_link1s="81e9fb486cb74b0738dee500ce01b64799b77400"
post_url=requests.get(f'https://link1s.com/api?api={api_token_link1s}&url={url}').json()
if post_url['status']=="error":
        print(post_url['message'])
        quit()
else:
        link_key=post_url['shortenedUrl']
nhap_key=input(f'''\033[1;32mLink Key: \033[1;33m{link_key}
\033[1;32mNhập Mã Key: \033[1;33m''')
if nhap_key==key:
        print('\033[1;32mChính Xác')
else:
        print('\033[1;31mKey Sai')
        quit()
os.system("clear")
logo = """
    \033[1;91m  (c).-.(c)             ░██████╗░░█████╗░██╗░░░░░░█████╗░
    \033[1;95m   / ._. \              ██╔════╝░██╔══██╗██║░░░░░██╔══██╗
    \033[1;33m __\( Y )/__            ██║░░██╗░███████║██║░░░░░██║░░██║
    \033[1;91m(_.-/'-'\-._)           ██║░░╚██╗██╔══██║██║░░░░░██║░░██║
    \033[1;92m   ||   ||              ╚██████╔╝██║░░██║███████╗╚█████╔╝
    \033[1;97m _.' `-' '._            ░╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░
    \033[1;95m(.-./`-'\.-.)      █░█ ▄▀█ █▀█   ▀█▀ █░█ ▄▀█ █    ▀█▀ █▀█ █▀█ █░░
    \033[1;93m `-'     `-'       █▀█ █▀█ █▄█   ░█░ █▀█ █▀█ █    ░█░ █▄█ █▄█ █▄▄ 
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\033[1;37m[\033[1;31m+\033[1;37m] \033[1;33mTool Đang Vận Hành Là: \033[1;31Auto Rpwliker 
\033[1;32mBox Zalo: \033[1;36mhttps://zalo.me/g/zhdkjl159
\033[1;32mZalo Admin: \033[1;36m0353550647
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
print(logo)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;91mCẢM ƠN CÁC CẬU ĐÃ TIN TƯỞNG SỬ DỤNG TOOL CỦA TỚ !")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
cookiefb=input("\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Cookie Facebook: \033[1;33m")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
cookie=input("\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Cookie Rpwliker: \033[1;33m")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
link=input("\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Link Post: \033[1;30m")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;32mType: like,love,haha,angry,wow,sad")
typelike=input("\033[1;37m[\033[1;31m+\033[1;37m]\033[1;32m Nhập Type Reaction: \033[0;33m")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
import json,requests,time
from time import strftime
ngay=int(strftime('%d'))
key=str(ngay*19032+1924)
print (key)
url=f'https://thaihao.online/keytoolfree.php?key={key}'
api_token_link1s="81e9fb486cb74b0738dee500ce01b64799b77400"
post_url=requests.get(f'https://link1s.com/api?api={api_token_link1s}&url={url}').json()
if post_url['status']=="error":
        print(post_url['message'])
        quit()
else:
        link_key=post_url['shortenedUrl']
nhap_key=input(f'''\033[1;32mLink Key: \033[1;33m{link_key}
\033[1;32mNhập Mã Key Để Vào Chạy: \033[1;33m''')
if nhap_key==key:
        print('\033[1;32mChính Xác')
else:
        print('\033[1;31mKey Sai')
        quit()
def rundelay(k):
  while (k>0):

    k=k-1
    print(f'\033[0;37m # \033[1;32m| \033[0;36mVui Lòng Đợi\033[1;33m '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[1;37m # \033[0;32m/ \033[1;36mVui Lòng Đợi\033[1;33m '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[0;37m # \033[1;32m- \033[0;36mVui Lòng Đợi\033[1;33m '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[1;37m # \033[0;32m\ \033[1;36mVui Lòng Đợi\033[1;33m '+str(k), end='\r')
    sleep(0.25)
tt=requests.post('https://id.traodoisub.com/api.php',data={
  "link":link
})
ttt=tt.json()["id"]
os.system("clear")
print(logo)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
headers={
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
t33=requests.get("https://rpwliker.com/feed",headers=headers).text
t4=t33.split(' <meta name="csrf-token" content="')[1].split('">')[0]
hd={
  "x-csrf-token":t4,
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
data={
  "send_to": link,
  "quantity": "100",
  "reaction_type[]": typelike,
  "local_only": "0",
  "relevant_accounts_only": "0"
}
stt=0
while True:
  stt=stt+1
  t3=requests.post("https://rpwliker.com/autoreaction",headers=hd,data=data).text
  sleep(10)
  check_dv = requests.get(f'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={ttt}&hash=AeTkxnH8LFuk5Gk10G0&refid=13', headers = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'save-data': 'on',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cookie': cookiefb
                        }).text
  t=check_dv.split('role="button" aria-pressed="true" href="')[1].split('">Tất cả ')[0]
  t2=t.split('total_count=')[1].split(' ')[0]
  print(f"\033[1;32mRPWLIKER  \033[1;37m[\033[1;31m{stt}\033[1;37m] \033[1;35m=> \033[1;32mSUCCESS \033[1;33m+ 100 \033[1;35m=> \033[1;32mTổng \033[1;33m{t2} \033[1;32mReactions")
  k=550
  rundelay(k)