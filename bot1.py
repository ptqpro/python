import os,sys,json,requests
from time import sleep
token_tds="TDS0nI3IXZ2V2ciojIyVmdlNnIsIyZiZzayUGbpFGdiojIyV2c1Jye"
info_tds=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token_tds).json()
if "success" in info_tds:
  user=info_tds['data']['user']
  xu=int(info_tds['data']['xu'])
else:
  print('\033[1;31mToken Không Hợp Lệ')
  exit()
token_fb="EAAAAZAw4FxQIBAJT2R9xMcoFVcdsGMKZBTWnBCK3ecCdXkbG3CviOPjqIuC8tYfnxhyAhWcQ0i3i6YhnPmYLMzQd95YNT2F6EF5YeCuVGMSdhEtcYAc231kDmQHIZBCZCX9Qepm2ZBgCRhCbSmZB33or5qVfveK5GBL1QnoRhXGocmfeoEEM5FvZCnoE1SHbZCkZD"
check_fb=requests.get('https://graph.facebook.com/me/?access_token='+token_fb).json()
if "id" in check_fb:
  idfb=check_fb['id']
  namefb=check_fb['name']
  đặt_nick = requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+token_tds).json()
  if "success" in đặt_nick:
    print ('\033[1;32m Đang Chạy Facebook: '+namefb)
    sleep(1)
  else:
    print ('\033[1;31m Cấu Hình Thất Bại Facebook: '+namefb)
else:
  print('\033[1;31m Token Die or Văng Acc')
os.system('clear')
print ('\033[1;32m Tên Tài Khoản: \033[1;33m'+user)
print ('\033[1;32m Số Xu Hiện Tại: \033[1;33m'+str(xu))
print ('\033[1;32m Facebook : \033[1;33m'+namefb)
print ('\033[1;32m ID Facebook: \033[1;33m'+str(idfb))
while (True):
  get_like=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+token_tds).json()
  for get in get_like:
    id_like = get['id']
    làm_nv=requests.post('https://graph.facebook.com/'+str(id_like)+'/subscribers?access_token='+token_fb)
    done_like=requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(id_like)+'&access_token='+token_tds).json()
    print (done_like)