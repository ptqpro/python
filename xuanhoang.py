#decode by le quang dung:)
import threading      
from time import sleep
import random
import os, sys
try:
        from selenium import webdriver
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.common.keys import Keys
except:
        os.system("pip install selenium")
        from selenium import webdriver
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.common.keys import Keys
def cls():
        os.system("cls")
q=open("so_tab.txt","r")
doc_q=q.read()
q.close()
if doc_q==0:
        cls()
        print("Số tab không thể bằng 0")
        sleep(3)
        quit()
def runtest(l):
        list_ten = ['Trình', 'Trịnh', 'Vĩnh', 'Viên', 'Yến', 'Linh', 'Mai', 'Tuyết', 'Anh', 'Ánh', 'Nam', 'Việt', 'Đức', 'Dương', 'Ngân', 
'Hoà', 'Nga', 'Hậu', 'Tú', 'Quân', 'Quốc', 'Hiển', 'Chương', 'Hà', 'Quê', 'Mùa', 'Bản', 'Liêm', 'Diệp', 'Nghĩa', 'Lợi']
        list_ho = ['Nguyễn', 'Trần', 'Huỳnh', 'Phan', 'Lê', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Ly', 'Cường', 'Tùng', 'Long', 'Dương', 'Duy', 'Minh', 'Hằng', 'Thảo', 'Yến']
        first_name_gm=random.choice(list_ho)
        last_name_hot=random.choice(list_ten)
        ll=["q","w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
        lll=["q","w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        l1=ll
        l2=ll
        l3=ll
        l4=lll
        l5=lll
        l6=lll
        l7=lll
        l8=lll
        l9=lll
        l10=lll
        l11=lll
        l12=lll
        l13=lll
        l14=lll
        l15=lll
        ok1=random.choice(l1)
        ok2=random.choice(l2)
        ok3=random.choice(l3)
        ok4=random.choice(l4)
        ok5=random.choice(l5)
        ok6=random.choice(l6)
        ok7=random.choice(l7)
        ok8=random.choice(l8)
        ok9=random.choice(l9)
        ok10=random.choice(l10)
        ok11=random.choice(l11)
        ok12=random.choice(l12)
        ok13=random.choice(l13)
        ok14=random.choice(l14)
        ok15=random.choice(l15)
        tk_hot=ok1+ok2+ok3+ok4+ok5+ok6+ok7+ok9+ok10+ok11+ok12+ok13+ok14+ok15
        ki_tu_mk=["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "B", "N", 
"M", "q","w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "$", "%", "&", "-", "+", "(", ")", "/", "*", ":", ";", "!", "?"]
        ki_tu_mk1=random.choice(ki_tu_mk)
        ki_tu_mk2=random.choice(ki_tu_mk)
        ki_tu_mk3=random.choice(ki_tu_mk)
        ki_tu_mk4=random.choice(ki_tu_mk)
        ki_tu_mk5=random.choice(ki_tu_mk)
        ki_tu_mk6=random.choice(ki_tu_mk)
        ki_tu_mk7=random.choice(ki_tu_mk)
        ki_tu_mk8=random.choice(ki_tu_mk)
        mk1=ki_tu_mk1
        mk2=ki_tu_mk2
        mk3=ki_tu_mk3
        mk4=ki_tu_mk4
        mk5=ki_tu_mk5
        mk6=ki_tu_mk6
        mk7=ki_tu_mk7
        mk8=ki_tu_mk8
        mk_hot=str(mk1)+str(mk2)+str(mk3)+str(mk4)+str(mk5)+str(mk6)+str(mk7)+str(mk8)
        first_name_hot=random.choice(list_ho)
        last_name_hot=random.choice(list_ten)
        while True:
                options=webdriver.ChromeOptions()
                options.add_argument("--app=https://outlook.live.com/owa/?nlp=1&signup=1")
                driver=webdriver.Chrome(options=options)
                x=l*400
                y=1
                driver.set_window_rect(x,y,400,550)
                driver.get("https://outlook.live.com/owa/?nlp=1&signup=1")
                sleep(2)
                hotmail=Select(driver.find_element_by_css_selector("#LiveDomainBoxList"))
                sleep(1.5)
                hotmail.select_by_value("hotmail.com")
                driver.find_element_by_css_selector("#MemberName").send_keys(tk_hot)
                sleep(1.5)
                driver.find_element_by_css_selector("#iSignupAction").click()
                sleep(2)
                driver.find_element_by_css_selector("#ShowHidePasswordCheckbox").click()
                driver.find_element_by_css_selector("#PasswordText").send_keys(mk_hot)
                driver.find_element_by_id("iSignupAction").click()
                sleep(1.5)
                driver.find_element_by_id("FirstName").send_keys(first_name_hot)
                driver.find_element_by_name("LastName").send_keys(last_name_hot)
                driver.find_element_by_id("iSignupAction").click()
                sleep(1.5)
                thang=Select(driver.find_element_by_css_selector("#BirthMonth"))
                list_thang=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                rd_thang=random.choice(list_thang)
                thang.select_by_value("2")
                day=Select(driver.find_element_by_css_selector("#BirthDay"))
                list_ngay=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
"21", "22", "23", "24", "25", "26", "28"]
                rd_ngay=random.choice(list_ngay)
                day.select_by_value(rd_ngay)
                list_nam= ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"]
                rd_nam=random.choice(list_nam)
                year=driver.find_element_by_css_selector("#BirthYear").send_keys(rd_nam)
                driver.find_element_by_css_selector("#iSignupAction").click()
                cls()
                print(f"Phá captcha tab: {str(l)} rồi enter")
                input()
                driver.find_element_by_css_selector("#idSIButton9").click()
                cls()
                tk_hotmail=tk_hot+"@hotmail.com"
                print(" Tài khoản: "+tk_hotmail)
                print("    Mật khẩu: "+mk_hot)
                with open("hotmaimail.txt", "a+", encoding="utf-8") as huhu:
                        huhu.write(tk_hotmail+"|"+mk_hot+"|"+first_name_hot+"_"+last_name_hot+"|"+rd_ngay+"."+rd_thang+"."+rd_nam+"|"+"\n")
                print("    Đã lưu hotmaimail.txt")
                driver.quit()
                out=input("    Nên fake ip rồi chạy tiếp nhé, enter để tiếp tục")
                if out=="":
                        os.system("python reg.py")
try:
        threads = []
        for l in range(int(doc_q)):
                threads += [threading.Thread(target=runtest,args={l},)]
        for t in threads:
                t.start()
        for t in threads:
                t.join()
except:
        print("Vui xem lại file so_tab.txt")