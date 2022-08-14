import random
from random import randint
from time import sleep
import os, sys
from selenium import webdriver
try:
	from selenium import webdriver
	from selenium.webdriver.support.ui import Select
	from selenium.webdriver.common.keys import Keys
except:
        print('Chưa Cài Thư Viện Vui Lòng Đợi')
        print('Sau Khi Cài Xong Vui Lòng Tắt Tool Và Khởi Động Lại')
        os.system("pip-3 install selenium")
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# List Color
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

# Background Tool
def logo():
    background = """ 
\033[1;92m╔══════════════════════════════════════════════════════════════╗ 
\033[1;95m  ______     _      __                ______            __
\033[1;92m /_  __/____(_)____/ /_____  _____   /_  __/___  ____  / /
\033[1;93m  / / / ___/ / ___/ //_/ _ \/ ___/    / / / __ \/ __ \/ / 
\033[1;96m / / / /  / / /__/ ,< /  __/ /       / / / /_/ / /_/ / /  
\033[1;91m/_/ /_/  /_/\___/_/|_|\___/_/       /_/  \____/\____/_/

\033[1;93m=========== \033[1;96mTool Register Hotmail By Nguyễn Hoàng \033[1;93m===========
           \033[1;91m© Desigin And Operation By Nguyễn Hoàng
\033[1;93m=============================================================
\033[1;92m ➽ Youtube: \033[1;92mTricker Tool
\033[1;97m ☛ Facebook: \033[1;97mnguyenhoang.user
\033[1;96m ☛ Zalo: \033[1;96m0347354556
\033[1;95m ☛ Momo: \033[1;95mTạm Ẩn

\033[1;92m╚══════════════════════════════════════════════════════════════╝"""
    for i in background: 
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.004)    

def background():
        logo = '''
\033[1;92m╔══════════════════════════════════════════════════════════════╗ 
\033[1;95m  ______     _      __                ______            __
\033[1;92m /_  __/____(_)____/ /_____  _____   /_  __/___  ____  / /
\033[1;93m  / / / ___/ / ___/ //_/ _ \/ ___/    / / / __ \/ __ \/ / 
\033[1;96m / / / /  / / /__/ ,< /  __/ /       / / / /_/ / /_/ / /  
\033[1;91m/_/ /_/  /_/\___/_/|_|\___/_/       /_/  \____/\____/_/

\033[1;93m =========== \033[1;96mTool Register Hotmail By Nguyễn Hoàng \033[1;93m===========
\033[1;93m ========== \033[1;91m© Desigin And Operation By Nguyễn Hoàng \033[1;93m==========

\033[1;92m╚══════════════════════════════════════════════════════════════╝'''
        for a in logo: 
                sys.stdout.write(a)
                sys.stdout.flush()
                sleep(0.004)
# Clear cmd
os.system('cls')
# Background
logo()
print('\n')
print('Đang Khởi Động Tool Register Hotmail')
sleep(0.09)

# Mở Trình duyệt
cai_dat = webdriver.ChromeOptions()
cai_dat.add_argument('--app=https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1651294196&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3deb891ad3-fdf7-5545-e2b8-e8536b83451a&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=D00479AACB309862&bk=1651294196&uiflavor=web&lic=1&mkt=VI-VN&lc=1066&uaid=23a136b5980140e9a30806afe7c3dde3')
hotmail = webdriver.Chrome(options=cai_dat)
hotmail.set_window_size(400, 600)
sleep(4)


# Chọn Hotmail
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/div/select/option[3]').click()
sleep(1)


# Clear cmd
os.system('cls')
# Background
background()
sleep(0.3)
print('\n')


# Điền Thông Tin Register Hotmail
print('Lưu Ý: ==> Không Được Tạo Tên Và Mật Khẩu Có Dấu Nhé <==')
user_hotmail = input('\nNhập Tên Tài Khoản Đăng Kí: ')
pass_hotmail = input('Nhập Mật Khẩu Đăng Kí: ')
# Nhập Tài khoản đăng kí
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input').send_keys(user_hotmail)
sleep(1)
hotmail.execute_script('document.querySelector("#iSignupAction").click()') # Ấn tiếp theo
sleep(5)
# Tạo Mật Khẩu
hotmail.execute_script('document.querySelector("#ShowHidePasswordCheckbox").click()') # Ấn hiện mật khẩu
hotmail.execute_script('document.querySelector("#iOptinEmail").click()') # Ấn chấp nhận các điều khoản của Hotmail
# Ấn tạo mật khẩu 
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]').send_keys(pass_hotmail)
sleep(1)
hotmail.execute_script('document.querySelector("#iSignupAction").click()') # Ấn tiếp theo 
sleep(3)


# Tạo thông tin đăng nhập
# Random Họ và Tên
list_ho = ['Bùi','Trần','Nguyễn','Họ','Phan','Uyên','Trung','Tủng','Sang','Đức','Mạnh','Lâm','Vũ','Minh',]
list_ten = ['Ân','Trung','Mào','Gà','Nhi','Nguyên','Giang','Trường','Triết','Kiệt','Johnny','Đặng','Đặt','Đậu',]
ho = random.choice(list_ho)
ten = random.choice(list_ten)
sleep(0.8)
# Điền Họ
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[1]/input').send_keys(ho)
sleep(0.7)
# Điền Tên
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[2]/input').send_keys(ten)
# Ấn tiếp tục
hotmail.execute_script('document.querySelector("#iSignupAction").click()')
sleep(3)


# Thông tin ngày tháng năm
# Random Ngày.Tháng.Năm
rd_ngay = random.randint(2, 32)
rd_thang = random.randint(2, 13)
rd_nam = random.randint(1985, 2005)
# Chọn Ngày
ngay = f'/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select/option[{rd_ngay}]'
hotmail.find_element_by_xpath(ngay).click()
sleep(0.5)
# Chọn Tháng
thang = f'/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select/option[{rd_thang}]'
hotmail.find_element_by_xpath(thang).click()
sleep(0.5)
# Chọn Năm
hotmail.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[3]/input').send_keys(rd_nam)
sleep(0.5)
# Ấn tiếp theo
hotmail.execute_script('document.querySelector("#iSignupAction").click()')
sleep(0.5)


# Clear cmd
os.system('cls')
# Background
background()
sleep(0.5)
print('\n')


# Hiển thị thông báo giải Captcha
print('Tránh Để Bị Delay Do Mạng Yếu Hoặc Chậm Nên Không Có Auto Captcha Và Mình Chưa Phát Triển Được ;-;')
sleep(0.2)
print('Mong Mọi Người Thông Cảm Và Cảm Ơn ^_^') 
sleep(0.2)
print('Mọi Người Giải Captcha Giúp Mình Nhé :33')
sleep(5)

# Clear cmd
os.system('cls')
# Background
background()
sleep(0.05)

# Giải Captcha xong thì ấn Enter
end_register = input('\nNếu Đã Giải Captcha Xong Vui Lòng Ấn Enter')
if end_register == '':
        hotmail.execute_script('document.querySelector("#idSIButton9").click()')
else: 
        print('Đã Xảy Ra Lỗi Vui Lòng Chạy Lại Tool')
sleep(1)

# Clear cmd
os.system('cls')
# Background
logo()
print('\n')
sleep(0.3)

# Lưu Tài khoản và Mật khẩu
with open('Register Hotmail.txt','a', encoding= "utf-8") as account_hotmail:
   account_hotmail.write('\n'+user_hotmail+'@hotmail.com')
   account_hotmail.write('|'+pass_hotmail)
   account_hotmail.write('|'+ho+ ' ' +ten)
   account_hotmail.write('|'+ str(rd_thang)+'.'+str(rd_thang)+'.'+str(rd_nam)+'\n')

# Hiện thông tin lưu tài khoản và mật khẩu
print('Thông Tin User Và Password Đăng Kí Đã Lưu Vào File: Register_Hotmail.txt ')
print('User: ',user_hotmail)
print('Password: ',pass_hotmail)
print('\nNếu Muốn Register Tiếp Thì Fake IP Để Tránh Xảy Ra Lỗi Hoặc Bị Chặn IP')
print('Cảm Ơn Bạn Đã Sử Dụng Tool ^_^')
sleep(0.5)
hotmail.quit()