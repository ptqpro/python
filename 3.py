#code tool của quân k7 ml nha, edit lại bởi hào thái 5cm nha, còn phương 20cm share tool nhé<333
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
try:
	import requests
except:
	os.system('pip install --upgrade pip && pip install requests')
	import requests
os.system("clear")
# Tool 
def logo():
    log="""

\033[1;92m▒█▀▀█ ▒█░▒█ ▒█░▒█ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀█                  
\033[1;92m▒█▄▄█ ▒█▀▀█ ▒█░▒█ ▒█░░▒█ ▒█▒█▒█ ▒█░▄▄                   
\033[1;92m▒█░░░ ▒█░▒█ ░▀▄▄▀ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄█

"""
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
       
       
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear') 

clr()
logo()
o=open('tokenfb.txt', "a+")
o.close()
a = 0
stt=0
print('\033[1;33m Vui Lòng Thêm Token Vào File "\033[1;36m tokenfb.txt \033[1;33m". Mỗi Dòng 1 Token !!!')
while(True):
  input('\033[1;33m Làm Xong Hoặc Có Sẵn Token Vui Lòng Ấn Enter')
  dulieu = open('tokenfb.txt',mode='r').read().split('\n')
  if dulieu == ['']:
     print('\033[1;31m Vui Lòng Thêm Token Vào Rồi Mới Nhấn Enter')
  else:
     print('\033[1;33m Tìm Thấy \033[1;36m'+str(len(dulieu))+' \033[1;33m Token Facebook')
     break
print("\033[1;31m«===================================================================»")
id = input(" \033[1;31m➻\033[1;31m❥ \033[1;33mNhập Link:\033[1;33m ")
def share(i):
    headers ={
       'authority': 'graph.facebook.com',
       'cache-control': 'max-age=0', 
       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
       'sec-ch-ua-mobile': '?0', 
       'upgrade-insecure-requests': '1',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
       'sec-fetch-site': 'none',
       'sec-fetch-mode': 'navigate',
       'sec-fetch-user': '?1', 
       'sec-fetch-dest': 'document', 
       'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5' }
    access_token = dulieu[i]
    tg=datetime.now().strftime('%H:%M:%S')
    retu = requests.post(f"https://graph.facebook.com/me/feed?link={id}&published=0&access_token={access_token}",headers=headers).json()
    if 'id' in retu:
        print('\033[1;00m',retu)
    else:
       print('\033[1;31m Token Block Tính Năng Hoặc Link Post Sai!!!')
while (True):
	for i in range(len(dulieu)):
		khoitao = threading.Thread(target=share,args=(i,)).start()