import os, sys,re,json,random
import datetime,hashlib
import os,sys, re, requests, json, time
from time import sleep
from bs4 import BeautifulSoup as bs
from colorama import Fore
import json, re, sys,os
import time, hashlib, subprocess
from time import sleep
from tabnanny import check
from tkinter import messagebox
import threading
import random
try:
        import requests,pystyle
        import requests
        import colorama
        import bs4
        from datetime import datetime
except:
    os.system("pip install datetime")
    os.system('pip install requests && pip install bs4 && pip install pystyle')
    import requests
    from datetime import datetime
    os.system("clear")
       

def dk():
   a= "\033[1;91m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.00000000001)
   print()
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(sr+'Chờ '+r+' '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.0000002)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [\]          ',end='\r')
       sleep(0.0000002)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [|]          ',end='\r')
       sleep(0.0000002)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [/]          ',end='\r')
       sleep(0.0000002)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [🔥]          ',end='\r')
       sleep(0.0000002)
  except:
     sleep(dl)
     print(dl,end='\r')
s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+' '
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.00000000001)
os.system('CLs')
os.system('clear')
banner = r"""

            ████████╗███╗  ██╗██╗  ██╗
            ╚══██╔══╝████╗ ██║██║ ██╔╝
               ██║   ██╔██╗██║█████═╝
               ██║   ██║╚████║██╔═██╗
               ██║   ██║ ╚███║██║ ╚██╗
               ╚═╝   ╚═╝  ╚══╝╚═╝  ╚═╝

"""[1:]
Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, enter=True)
os.system('CLs')
os.system("clear")
dau="~ [✓] => "
def banner1():
 banner1 = f"""

         ██████╗  █████╗ ██╗   ██╗
        ██╔════╝ ██╔══██╗██║   ██║
        ██║  ██╗ ███████║██║   ██║
        ██║  ╚██╗██╔══██║██║   ██║
        ╚██████╔╝██║  ██║╚██████╔╝
         ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
\033[1;3m- - - - - - - - - - - - - - - - - - - - - - - - -
{dau}Tool Machine-Liker By : Gấu Tricker
{dau}Zalo : 0385598492
{dau}Ủng Hộ Lấy Động Lực Làm Tool 
{dau}Ví Momo : 0385598492
- - - - - - - - - - - - - - - - - - - - - - - - -\033[1;0m\n"""
 for X in banner1:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
#end banner
banner1();
sleep(0.2)
ck=input(dau+"Nhập Cookie Machine-Liker : ")
print("- "*25)
user=input(dau+"Nhập User-Agent : ")
print("- "*25)
link=input(dau+"Nhập Url Buff : ")
print("- "*25)
sleep(0.2)
os.system("clear")
banner1();
print(dau+"[1] LIKE ")
print(dau+"[2] LOVE")
print(dau+"[3] WOW")
print(dau+"[4] HAHA")
print(dau+"[7] SAD")
print(dau+"[8] ANGRY")
print(dau+"[16] Cre")
print("- "*25)
type=input(dau+"Nhập Cảm Xúc Muốn Buff P/s(1,2,3,16,..) : ")
print("- "*25)
dl=int(585)
def delay(dl):
   t=datetime.now().strftime("%H:%M")
   for ti in range(dl , -1, -1):
    print(f'\033[1;3m● [\] Vui Lòng Đợi {ti} Giây  ',end='\r')
    sleep(0.2)
    print(f'\033[1;3m● [/] Vui Lòng Đợi {ti} Giây  ',end='\r')
    sleep(0.2)
    print(f'\033[1;3m● [\] Vui Lòng Đợi {ti} Giây  ',end='\r')
    sleep(0.2)
    print(f'\033[1;3m● [/] Vui Lòng Đợi {ti} Giây  ',end='\r')
    sleep(0.2)
    print(f'\033[1;3m● [\] Vui Lòng Đợi {ti} Giây  ',end='\r')
    sleep(0.2)
def like(user,ck):
  a=requests.post("https://www.machine-liker.com/api/get-post-info/", headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck},data={"url":link})
  if "post" in a.text:
   id=a.json()["post"]["id"]
   st=a.json()["post"]["story"]
  else:
   exit(dau+"Die Cookie")
  url1=f"https://www.machine-liker.com/send-reactions/?post_id={id}&story={st}"
  a=requests.get(url1,headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck})
  obj=a.text.split('name="object_id" value="')[1].split('"')[0]
  d=0
  yeuthanhthuy=requests.post("https://www.machine-liker.com/api/send-reactions/",headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck},data={"object_id":obj,"reactions":type,"limit":"150"})
  if "info" in yeuthanhthuy.text:
   cong=yeuthanhthuy.text.split('message": "')[1].split(' reactions')[0]
   tong=yeuthanhthuy.json()["info"]["total_reactions"]
   t=datetime.now().strftime('%H:%M:%S')
   print(f" ~ [Trương Khánh] </> [{t}] </> +{cong} Cảm Xúc Vào Bài Viết")
   print(f" ~ [Trương Khánh] </> ID Bài Viết : {id}")
   print(f" ~ [Trương Khánh] </> Loại Cảm Xúc Đang Làm : {type}")
   print(f" ~ [Trương Khánh] </> Tổng Reaction : {tong}")
   print(f"- - - - - - - - - - - - - - - - - - - - - - - - -")
   delay(dl);
  else:
   t=datetime.now().strftime('%H:%M:%S')
   print(f" ~ [Trương Khánh] </> [{t}] </> Thất Bại")
   delay(dl);
while True:
 print(dau+"Đang Login Web Waiting...",end="\r")
 like(user,ck);
