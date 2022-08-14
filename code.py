import os, sys,re,json,random
from time import sleep
import threading
try:
	import requests,pystyle
except:
	os.system('pip install requests && pip install bs4 && pip install pystyle')
	
def dk():
   a= "\033[1;91m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(sr+'Chờ '+r+' '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [\]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [|]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [/]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [🔥]          ',end='\r')
       sleep(0.2)
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
     sleep(0.001)
   print()
os.system('clear')                          
def logo():
    logo = """       """
    ra(logo)

dk()
from pystyle import Box
os.system('clear')
logo()
dk()
print("- - - - - - - - - - - TDS && TTC - - - - - - - - - - - - -")
print()
print(sr+"Nhập [1] TDS 3.4 [Multi Token] [MaxSpeed 0.4s]")
print(sr+"Nhập [2] TTC 2.3 [Multi Token] [MaxSpeed 0s]")
print()
print("- - - - - - - - - - - Buff Share - - - - - - - - - - - - -")
print()
print(sr+"Nhập [3] Share 1.5 [Clone, Via] [Ảo] [MaxSpeed 1s/200Share] ")
print(sr+"Nhập [4] Share 1.3 [Clone, Via] [Thật] [MaxSpeed 1s/200Share]")
print(sr+"Nhập [5] Share 1.6 [Page] [Thật] [MaxSpeed 1s/20Share]")
print()
print("- - - - - - - - - - - Buff Comment - - - - - - - - - - - -")
print()
print(sr+"Nhập [6] Cmt 2.3 [Page] [Thật] [MaxSpeed 1s/200Cmt]")
print(sr+"Nhập [7] Cmt 2.4 [Clone, Via] [MaxSpeed 1s/200Cmt]")
print()
print("- - - - - - - - - - - - - Page - - - - - - - - - - - - - -")
print()
print(sr+"Nhập [8] RegPage 2.8 [Thường] [Multi Cookie] [1s/10Page]")
print(sr+"Nhập [9] RegPage 3.2 [Vị Trí] [Multi Token - ID] [1s/10Page]")
print(sr+"Nhập [10] FollowPage 1.2 [Multi Cookie] [1s/100Follow]")
print()
print("- - - - - - - - - - - Facebook - - - - - - - - - - - - -")
print()
print(sr+"Nhập [11] Tool Nuôi Facebook 1.2 [Cookie]")
print(sr+"Nhập [12] Tool Auto Thêm Bạn Gợi Ý 1.1 [Cookie]")
print(sr+"Nhập [13] Lọc Bạn Bè Không TT [Cookie]")
print()
print("- - - - - - - - - - - - More - - - - - - - - - - - - - -")
print()
print(sr+"Nhập [14] Tool TopView 1.1 ")
print(sr+"Nhập [15] Tool TubeRocket 1.3")
print()
print("- - - - - - - - - - - - ME - - - - - - - - - - - - - - -")
print()
print(sr+"Zalo Cá Nhân : 0359265155")
print()
dk()
abc = int(input(sr+"Nhập Số : "))
dk()                                                              
try:
  if abc == 1:
    exec(requests.get("https://run.mocky.io/v3/3ad741a8-afc2-4040-8f93-b58af94cc01a").text)
  if abc == 2:
    exec(requests.get("https://run.mocky.io/v3/9c59d984-0352-4e10-820c-63c5b8b14843").text)
  if abc == 3:
    exec(requests.get("https://run.mocky.io/v3/d7de67b6-65d1-47d8-b992-272c7e9f4df3").text)
  if abc == 4:
    exec(requests.get("https://run.mocky.io/v3/76acfd91-9e8f-4fca-b934-b94fe786d381").text)
  if abc == 5:
    exec(requests.get("https://run.mocky.io/v3/9097a374-a648-45e5-99d1-7f5373e38804").text)
  if abc == 6:
    exec(requests.get("https://run.mocky.io/v3/0c8b4cca-e375-468d-8ddd-6af73a2487b7").text)
  if abc == 7:
    exec(requests.get("https://run.mocky.io/v3/dac87168-2c3b-4e05-950f-329700c61d65").text)
  if abc == 8:
    exec(requests.get("https://run.mocky.io/v3/4cec6476-780a-4f8e-a59d-9b6db8be62a0").text)
  if abc == 9:
    exec(requests.get("https://run.mocky.io/v3/49204ca8-e8b5-495e-bded-eece94bd2f57").text)
  if abc == 10:
    exec(requests.get("https://run.mocky.io/v3/5a9eb351-c486-4ca6-8f5b-3ca42f3b2f03").text)
  if abc == 11:
     print(sr+"Tool Đang Bảo Trì")
  if abc == 12:
     print(sr+"Tool Đang Bảo Trì")
  if abc == 13:
     print(sr+"Tool Đang Bảo Trì")
  if abc == 14:
    exec(requests.get("Tool Đang Bảo Trì").text)
  if abc == 15:
    exec(requests.get("Tool Đang Bảo Trì").text)

except:
   pass


