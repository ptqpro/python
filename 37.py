from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
black='\033[1;90m'
white='\033[1;97m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
whitex='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
fivex=white+'['+blue+'FIVEX'+white+']'
fivex_no_pro=whitex+'[FIVEX]'+end
hln=white+"["+blue+"HOÀNG LONG NGŨ"+white+"]"
def logo():
    log="""               \033[7;37m\033[1;37m HOÀNG LONG NGŨ [FIVEX] \033[0m \n               \033[4;40;97m\033[1;97m 0  3  0  4  2  0  0  5 \033[0m \n               \033[4;40;96m\033[1;96m MB BANK  :  \033[1;97m8603042005 \033[0m \n               \033[4;40;97m\033[1;97m Z A L O  :  \033[1;96m0979762905 \033[0m \n               \033[7;37m\033[1;37m T O O L  :  TDS PYTHON \033[0m \n \n"""
    os.system('clear')
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.001)
logo()
print(fivex,'VUI LÒNG ĐỢI !',end='\r')
print('Tool Đã Bị Dec bởi Triệu Đức Dũng đang vào tool vui lòng chờ ')
for dvt in range(3,0,-1):
        print(blue+'[FIVEX]',white+'['+blue+str(dvt)+white+']',end='\r')
        sleep(0.7)
logo()
while(True):
        token_tds=input(white+'NHẬP'+blue+' ACCESS_TOKEN TDS: '+white)
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds))
        if 'error' in ttacc.text:print(red+ttacc.json()['error'].upper())
        if 'success' in ttacc.text:
                logo()
                user=ttacc.json()['data']['user']
                xu=ttacc.json()['data']['xu']
                xu_die=ttacc.json()['data']['xudie']
                print(white+'['+blue+'USER: '+white+user.upper()+blue+']'+white+'['+yellow+xu+' XU'+white+']'+black+'['+xu_die+' XU DIE'+white+']')
                sleep(1)
                break
logo()
while(True):
        while(True):
                while(True):
                        ck_fb=input(blue+'NHẬP'+white+' COOKIE FACEBOOK: '+blue)
                        if ck_fb=='':break
                        u_check='https://mbasic.facebook.com/profile.php'
                        h={'cookie':ck_fb}
                        check=requests.get(url=u_check,headers=h).text
                        if 'Trang cá nhân' in str(check):
                                cookie=ck_fb.split(';')
                                for o in range(0,len(cookie)):
                                        if 'c_user' in cookie[o]:
                                                get_id_fb=cookie[o].split('=')
                                                id_fb=get_id_fb[1]
                                break
                        else:
                                print(fivex,white+'['+red+'COOKIE FACEBOOK DIE'+white+']')
                if ck_fb=='':
                        print(white+'THANKS BẠN ĐÃ SỬ DỤNG TOOL CỦA',fivex+' !')
                        quit()
                logo()
                u_run='https://traodoisub.com/api/?fields=run&id='+id_fb+'&access_token='+token_tds
                print(white+'['+blue+'ĐANG'+white+' CẤU HÌNH'+blue+' ID: '+white+id_fb+blue+']')
                run=requests.get(url=u_run)
                if 'success' in run.text:
                        print(fivex,'['+run.json()['data']['msg'].upper()+']')
                        sleep(0.5)
                        break
                else:
                        print(red+run.json()['error'].upper())
        logo()
        stop=int(input(white+'NHẬP '+blue+'SỐ NHIỆM VỤ: '+white))
        delay=int(input(blue+'NHẬP '+white+'DELAY: '+blue))
        s=0
        logo()
        while(True):
                print(fivex,'ĐANG GET LIST NHIỆM VỤ, VUI LÒNG ĐỢI !',end="\r")
                while(True):
                        try:
                                list_nv=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+token_tds)
                                if 'id' in list_nv.text:break
                        except:
                                print(fivex_no_pro+white+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+white+']','               ',end='\r')
                for x in range(0,len(list_nv.json())):
                        try:
                                id_post=list_nv.json()[x]['id']
                                type_post=list_nv.json()[x]['type']
                                if str(type_post)=='LIKE':
                                        type_rect='LIKE'
                                        v=1
                                if str(type_post)=='LOVE':
                                        type_rect='LOVE '
                                        v=2
                                if str(type_post)=='CARE':
                                        type_rect='CARE '
                                        v=3
                                if str(type_post)=='HAHA':
                                        type_rect='HAHA '
                                        v=4
                                if str(type_post)=='WOW':
                                        type_rect='WOW  '
                                        v=5
                                if str(type_post)=='SAD':
                                        type_rect='SAD  '
                                        v=6
                                if str(type_post)=='ANGRY':
                                        type_rect='ANGRY'
                                        v=7
                                host='https://mbasic.facebook.com'
                                u=host+'/reactions/picker/?is_permalink=1&ft_id='+id_post
                                h={'cookie':ck_fb}
                                check=requests.get(url=u,headers=h).text
                                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        break
                                if 'Phẫn nộ' in check:
                                        cx=BeautifulSoup(check,'html.parser')
                                        type_cx=cx.find_all('a')
                                        u_cx=host+str(type_cx[v]['href'])
                                        rect=requests.get(url=u_cx,headers=h).text
                                        #print(rect)
                                        #1like_2tym_3thuongthuong_4haha
                                        #5wow_6sad_7phanno
                                nhan_tien=requests.get('https://traodoisub.com/api/coin/?type='+type_post+'&id='+id_post+'&access_token='+token_tds)
                                if 'success' in nhan_tien.text:
                                        s=s+1
                                        xu=str(nhan_tien.json()['data']['xu'])
                                        msg=str(nhan_tien.json()['data']['msg']).upper()
                                        time=datetime.now().strftime("%H:%M:%S")
                                        print(fivex_no_pro+white+'['+blue+str(s)+white+']['+time+']['+blue+type_rect+white+']['+yellow+msg+white+']['+yellow+xu+white+']','     ')
                                        if s==stop:break
                                        for a in range(delay,0,-1):
                                                print(fivex,'['+blue+str(a)+white+']','     ',end='\r')
                                                sleep(0.7)
                        except:
                                print(fivex_no_pro+white+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+white+']','               ',end='\r')
                if s==stop:break
                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        print(fivex_no_pro+white+'['+red+'COOKIE FACEBOOK DIE'+white+']','                    ')
                                        break
        print(fivex+white+'[DỪNG TOOL ẤN'+blue+' ENTER !!!'+white+']')
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
        if s==stop:print(fivex_no_pro+white+'[CHẠY TOOL SUCCESS, TỔNG XU:',yellow+str(ttacc['data']['xu'])+']')