import requests,random,os
from threading import Thread
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Joy 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'}
nuoc=['af_ZA', 'ge', 'ar', 'id_ID', 'az', 'it', 'cz', 'ja', 'de', 'ko', 'de_AT', 'lv', 'de_CH', 'nb_NO', 'el', 'en', 'nl', 'en_AU', 'nl_BE', 'pl', 'pt_BR', 'en_CA', 'pt_PT', 'en_GB', 'ro', 'en_IE', 'ru', 'sk', 'en_US', 'sv', 'en_ZA', 'tr', 'es', 'uk', 'es_MX', 'vi', 'fa', 'zh_CN', 'fr', 'zh_TW', 'fr_CA', 'zu_ZA', 'fr_CH']
while True:
    print(nuoc)
    huy=input('Không thích nước nào thì điền kí tự nước đấy để không đào: ')
    if huy=='':break
    elif huy not in nuoc:print('Làm gì có nước này?:))')
    else:nuoc.remove(huy)
    os.system('clear')
duoi=input('Đuôi: ')
HaHa=input('File chứa mail: ')
luong=int(input('Luồng: '))
def daomail():
    while True:
        try:
            luu=''
            data={
    'number':'1000',
    'culture':random.choice(nuoc),
    '__RequestVerificationToken':'CfDJ8Fud5pe4-RhHmVzQ3TlWMhkmfRE2OznEA7IgRl6PRzPhGcDnx897Ql8DiCoJV2DDV7Moa0O8qEL-iV99WqW3coPB_St7QfiiaZUX9cO8zrlbVBUWXjoAhIw8EauhBy9QymoepO_KDiK2JuavbMkVvEA',
    'X-Requested-With':'XMLHttpRequest'
            }
            trave=requests.post('https://randommer.io/random-email-address',headers=headers,data=data).json()
            for RT in trave:
                loz=RT.split('@')[0]
                if len(loz)<5:break
                loz+=f'@{duoi}\n'
                luu+=loz
                print(loz,end='')
            open(HaHa,'a+').write(luu)
        except:pass
for WHIST in range(luong):
    Thread(target=daomail).start()