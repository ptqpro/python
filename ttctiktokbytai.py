import requests
from requests import get,post
list_job_follow=[] #dùng để gộp các id post sau khi làm job follow để nhận xu
list_job_tym=[] #dùng để gộp các id post sau khi làm job tym để nhận xu

#login bằng access token 
token_ttc="58692fcccffded71092aedb7a05de9db"
pon=post('https://tuongtaccheo.com/logintoken.php',data={'access_token':token_ttc})
cookie=pon.headers['Set-cookie'] #cookie dùng để lấy job
pon=pon.json()
headers={
    "x-requested-with":"XMLHttpRequest",
    "cookie":cookie
    }
    
#check token trc
if pon['status'] == "success": #nếu đúng thì
	user = pon['data']['user'] #user của access token
	xu = pon['data']['sodu'] #số xu
else: #nếu token sai sẽ print lời nhắn từ api
	print(f"\033[1;31m {pon['mess']}")
	quit()
	
	
#lấy job follow
get_job_fl=get('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php', headers=headers).json() #lấy job
for nv in get_job_fl:
	id_post = nv['idpost'] #id của job
	user_tik = nv['link'] #user tiktok cần follow
	link_user = f'https://www.tiktok.com/@{user_tik}' #link đầy đủ của user cần follow
	#làm job gắn dô đâyy
	
	
	#z thoy
	#sau khi làm job
	list_job_follow.append(id_post) #thêm id post vào danh sách id đêt nhận xu
	if len(list_job_follow) >= 10: #nếu số job đã làm lớn hơn hoặc = 10
		list_id_follow = ','.join(list_job_follow)
		check_follow = post('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php', data = {'id': list_id_follow})
		if 'Thành công' in check_follow.text: #nếu có chữ Thành công trong check nhận xu
			xu_cong=check_follow.json()['sodu'] #số xu đc cộng
			print(f'Cộng {xu_cong}')
		else:
			print('Nhận thất bại') #nhận thất bại
	
#lấy job tym
get_job_tym = get('https://tuongtaccheo.com/tiktok/kiemtien/getpost.php', headers = headers).json() #lấy job tym
for tym in get_job_tym:
	id_post_tym = tym['idpost'] #id của job
	link_video = tym['link'] # link video tik tok cần tym
	#làm job gắn dô đâyy
	
	
	#z thoy
	#sau khi làm job
	if len(list_job_tym) >= 5: #nếu số job đã làm lớn hơn hoặc = 10
		list_id_tym = ','.join(list_job_tym)
		check_tym = post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', data = {'id': list_id_follow})
		if 'Thành công' in check_tym.text: #nếu có chữ Thành công trong check nhận xu
			xu_cong=check_tym.json()['sodu'] #số xu đc cộng
			print(f'Cộng {xu_cong}')
		else:
			print('Nhận thất bại') #nhận thất bại