
import requests
import os, sys,time
try:
  from faker import Faker
  from requests import session
  import requests, random, re
  from random import randint
  import concurrent.futures
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
from faker import Faker
from requests import session
import requests, random, re
from random import randint
from random import choice
import concurrent.futures
import random
import secrets

def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
print(" \033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;39m")
print("\033[1;94m=>>Tao Là Trùm Check Mail")
try:
 n_valid = 0
 fileEmail = open(input("•Nhập File Chứa Mail Liên Kết (ex: mail.txt) : ")).readlines()
 print("\033[1;32m Vui Lòng Lọc Liên Kết Ảo Trước Khi Chạy ")
 valid = input(" •Nhập File Lưu Mail Mã(ex: mailma.txt) : ")
 clear()
 print("\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;32m=\033[1;31m=\033[1;39m")
 print (" [••]🐌Đang Chạy🐌[••] ")
except:
    print (" \033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP ẢO đá Hả !")
    quit()
for email_fb in fileEmail:
 n_valid += 1
 head1={'Host':'d.facebook.com',
'user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'x-requested-with':'mark.via.gp',
'dnt':'1',
'sec-fetch-site':'none',
'sec-fetch-mode':'navigate',
'sec-fetch-user':'?1',
'sec-fetch-dest':'document',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'}
 a1 = requests.get(url="https://d.facebook.com/",headers=head1)
 ckfb = a1.headers['set-cookie'].split('; sb=')[0]+';'+a1.headers['set-cookie'].split('sb=')[1].split(';')[0]+';'
 head2 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':ckfb}
 head3 = {'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://d.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr','accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7','cookie':ckfb}
 a1 = requests.get(url="https://d.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr",headers=head3)
 lsd = a1.text.split('name="lsd" value="')[1].split('"')[0]
 jazoest = a1.text.split('name="jazoest" value="')[1].split('"')[0]
 reg_impression_id = a1.text.split('name="reg_impression_id" value="')[1].split('"')[0]
 reg_instance = a1.text.split('name="reg_instance" value="')[1].split('"')[0]
 da2 = {'lsd':lsd,'jazoest':jazoest,'cpp':'2','reg_instance':reg_instance,'submission_request':'true','helper':'','reg_impression_id':reg_impression_id,'ns':'0','zero_header_af_client':'','app_id':'','logger_id':'','field_names[]':'firstname','field_names[]':'reg_email__','field_names[]':'sex','field_names[]':'birthday_wrapper','field_names[]':'reg_passwd__','lastname':'Hảo','firstname':'Hán','reg_email__':email_fb,'sex':'2','custom_gender':'','did_use_age':'false','birthday_day':'19','birthday_month':'10','birthday_year':'1998','age_step_input':'','reg_passwd__':'','submit':'Đăng+ký'}
 a2 = requests.post(url="https://d.facebook.com/reg/submit/?cid=103",headers=head2,data=da2).text
 if 'mật khẩu' in a2:
    print("\033[1;35m Về Mã Này Ngon Haha: " + email_fb + "\033[1;35m")
    open(valid,"a").write(email_fb)
 else:
    print("\033[1;30m Mail Lỏ Cặc Rồi Bỏ  : " + email_fb + "\033[1;30m")
 