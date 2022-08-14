import requests,os
from time import sleep
from datetime import datetime
import os, sys, re, json
try:
  import pystyle
  import requests
  import googletrans
  import bs4
except:
  os.system('pip install requests && pip install pystyle && pip install googletrans && pip install bs4')
from datetime import datetime
import datetime,base64
import threading
from time import sleep
import requests,re,json,random,sys,os
from time import sleep
from time import sleep
from datetime import datetime
import random
import requests, os, sys, re, json
from threading import Thread
import threading
import time
from random import choice, randint, shuffle
import json,requests,time
from time import strftime
os.system('clear')
#-------------------------------Màu------------------------------#
vang='\033[1;33m'
trang='\033[1;97m'
do='\033[1;91m'
luc='\033[1;32m'
xanh='\033[1;36m'
icon='\033[1;91m[\033[1;33m⟨⟩\033[1;91m] \033[1;97m=>\033[1;92m '
#-------------------------------Logo------------------------------#
def logo():
	tg=datetime.now().strftime('%H:%M:%S')
	os.system('clear')
	

while True:
	print('                                             ',end='\r')
	tokentds = input(icon+luc+'Nhập Token Tds:'+vang+' ')
	log=requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={tokentds}').json()
	if 'success' in log:
		user=log['data']['user']
		xu=log['data']['xu']
		xudie=log['data']['xudie']
		print(xanh+'Đăng Nhập Thành Công')
		print(do+'─'*50)
		sleep(1)
		break
	else:
		
		print(do+'Đăng Nhập Thất Bại')
		print(do+'─'*50)



while True:
	cookie_tiktok=input(icon+luc+'Nhập Cookie Tiktok:'+vang+' ')
	try:
		tt_csrf_token=cookie_tiktok.split('tt_csrf_token=')[1].split(';')[0]
		get_id=requests.get('https://www.tiktok.com/',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_tiktok,'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1',}).text
		id_tiktok=get_id.split('"uid":"')[1].split('"}')[0]
		break
	except:
		
		print(do+'Tự Động Get Id Tiktok Thất Bại, Vui Long Nhập Đúng Cookie!')
		print(do+'─'*50)
while(True):
	logtiktoktds=requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={id_tiktok}&access_token={tokentds}').json()
	if 'success' in logtiktoktds:
		msg=logtiktoktds['data']['msg']
		print(xanh+msg)
		sleep(1)
		break
	else:
		
		print(do+logtiktoktds['error'])
		print(do+'─'*50)
os.system('clear')
logo()
print(icon+luc+f'''Tên Tài Khoản:{vang} {user}
{icon}{luc}Xu Hiện Tại: {vang}{xu}
{icon}{luc}Xu Bị Trừ: {vang}{xudie}''')
print(do+'─'*50)
delay = int(input(icon+luc+'Nhập Delay:'+vang+' '))
print(do+'─'*50)
stt=0

print(f'{luc}Đang Cấu Hình ID: {vang}{id_tiktok} ')
print(do+'─'*50)
while(True):
	try:
		def getJobFollow(tokentds: str):
			while(True):
				a=requests.get(f'https://traodoisub.com/api/?fields=tiktok_follow&access_token={tokentds}').json()
				if 'countdown' in a:
					pass
				else:
					break
			return a['data']
		getJob=getJobFollow(tokentds)
		for x in getJob:
			id_job = x['id']
			id_auto = id_job.split('_')[0]
			tg=datetime.now().strftime('%H:%M:%S')
			stt+=1
			print(f'{vang} [{trang}TOOL{vang}] {vang}[{trang}{stt}{vang}] {do}|{xanh} {tg} {do}| {do}{vang}FOLLOW{do} | {trang}{id_auto}{do} |')
			#print(a)
			for i in range(delay,0,-1):
				print(f'{vang} [{trang}NGOCTOOL{vang}] {vang}{i}','          ',end='\r')
				sleep(1)
			headers_autofl={'Host':'t.tiktok.com','Connection':'keep-alive','Content-Length':'0','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','content-type':'application/x-www-form-urlencoded','sec-ch-ua-mobile':'?0','tt-csrf-token':tt_csrf_token,'sec-ch-ua-platform':'"Linux"','Accept':'*/*','Origin':'https://www.tiktok.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.tiktok.com/','Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Cookie':cookie_tiktok}
			abc = requests.post(f"https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&browser_online=true&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=50&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=VN&referer=&region=VN&screen_height=883&screen_width=424&type=1&tz_name=Asia/Saigon&user_id={id_auto}",headers=headers_autofl).text
			cache_fl = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={id_job}&access_token={tokentds}').json()
			if stt % 10 == 0:
				sleep(3)
				b=requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={tokentds}').json()
				if 'success' in b:
					xuall=b['data']['xu']
					msg=b['data']['msg']
					
					print(do+'─'*50)
					
					
					print(f'\033[1;36m Nhận Thành Công \033[1;32m{msg} \033[1;31m|\033[1;33m {xuall}')
					print(do+'─'*50)
	except:
		print(do+'Đang Kiếm Thêm Nhiệm Vụ','     ',end='\r')