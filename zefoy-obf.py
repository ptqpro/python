from undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import random,os,requests,hashlib
from tkinter import messagebox
if __name__ == '__main__': 
        options = {}
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--force-dev-mode-highlighting") 
        chrome_options.add_argument("--system-developer-mode")
        chrome_options.add_argument("--headless")
        driver = Chrome(seleniumwire_options=options, options=chrome_options)
        driver.get('https://zefoy.com/')
        sleep(4)
        driver.save_screenshot('D:/Buff_View_TikTok/CaptchaCode02.png')
        print('Captcha được lưu ở file CaptchaCode02.png ')
        captcha = input('Nhập Captcha: ')
        link = input('Nhập Link TikTok: ')
        driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/form/div/div/div/input').send_keys(captcha),sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/form/div/div/div/div/button').click(),sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button').click(),sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div/form/div/input').send_keys(link),sleep(1)
        job = 0 
        while True:
                try:
                        now = datetime.now()
                        time = now.strftime(" %H:%M:%S")
                        driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div/form/div/div/button').click(),sleep(1)
                        driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div/div/div[1]/div/form/button').click(),sleep(1)
                        job = job + 1
                        print(f'[{job}] <> [{time}] <> Buff thành công +1000 view')
                except:
                        print('Đang Tiến hành Buff Lượt Tiếp Theo!', end='\r')
                        sleep(10)
                        continue