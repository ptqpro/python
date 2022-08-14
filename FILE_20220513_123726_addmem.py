from ast import Add
import os
try:
    import json
    import requests
    from time import sleep
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon import TelegramClient, functions, types, sync
    from telethon.errors import *
    from telethon.tl.types import PeerUser
    import sqlite3
except:
    os.system("pip install telethon")
    os.system("pip install requests")
def waiting(i):
    for w in range(i,0,-1):
        print(f"Chờ sau {w} giây!",end="\r")
        sleep(1)
class AddMem():
    def connect(self,phone):
        api_id = 2015084
        api_hash = '24e8f34925604e25a9b8d695b21cf333'
        client = TelegramClient("session/"+phone,api_id,api_hash)
        client.connect()
        return client
    def cr_session(self):
        while(True):
            print("==================================")
            phone = input("Nhập số điện thoại(+84358377824): ")
            client = self.connect(phone)
            if not client.is_user_authorized():
                try:
                    try:
                        client.send_code_request(phone)
                        client.sign_in(phone,input("Nhập code : "))
                    except SessionPasswordNeededError:
                        client.start(phone,input('Nhập mật khẩu 2FA:'))
                    print ("Tạo thành công session ")
                    with open("list.txt","a") as file:
                        file.write(phone+"\n")
                except Exception as e:
                    print(phone+" ",e)
            else:
                print ("Tạo thành công session từ trước")
            print("Mua acc Telegram liên hệ @nghiaplus")
            client.disconnect()
    def invite(self,client,user):

        result = client(functions.channels.InviteToChannelRequest(
            channel=gr,
            users=[user]))
        return result
    def main(self):
        z=0
        x=0
        while(True):
            try:
                phone = lst_phone[z]
                print(phone)
                client = self.connect(phone)
                if not client.is_user_authorized():
                    print("[!]- Session die!")
                    z=z+1
                    client.disconnect()
                else:
                    try:
                        client(JoinChannelRequest(channel))
                        client(JoinChannelRequest(gr))
                        result = client(functions.channels.GetParticipantsRequest(
                        channel=channel,
                        filter=types.ChannelParticipantsRecent(),
                        offset=42,limit=200,hash=0))
                        #ChannelParticipantsRecent
                        #ChannelParticipantsMentions
                        print("Get",len(result.users), "member")
                        msg = ""
                        limit = 0
                        for user in result.users:
                            if x >= len(result.users):
                                print(f"ĐÃ QUÉT HẾT MEM TRONG GROUP {channel}, VUI LÒNG ĐỔI GROUP LẤY MEM HOẶC MUA BẢN PRO ĐỂ KÉO TIẾP,ok!")
                                dvc = 'https://t.me/result_id'
                                client(JoinChannelRequest(dvc))
                                client.send_message(dvc,"@"+gr+"\n"+channel)
                                client(functions.channels.LeaveChannelRequest(
                                channel=dvc))
                                client.disconnect()
                                exit()
                            usn = str(user.username)
                            id = str(user.id)
                            with open('id_'+gr+'.txt',"r") as idds:
                                lst_id_used = idds.read()
                            
                            if id in lst_id_used:
                                x=x+1
                                print(f"[{x}]- Đang quét user [{usn}]     ",end="\r")
                            else:
                            
                            #ent   = client.get_entity(PeerUser(id_))
                                try:
                                    
                                    rss = self.invite(client,user)
                                    if rss.updates != []:
                                        print(f"[{x}]->>>> Mời thành công {usn}!             ")
                                        
                                        if usn != "None":
                                            msg= msg+usn+"\n"
                                    else:
                                        print(f"[{x}]->>>>> Mời {usn}                   ")
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    limit = limit+1

                                    if limit == lm:
                                        print("Kéo xong {} thành viên, chuyển sang acc khác!".format(lm))
                                        z=z+1
                                        break

                                    waiting(i)
                                except UserPrivacyRestrictedError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f'[{x}]- {usn} Quyền Riêng Tư Của Người Dùng')
                                except UserChannelsTooMuchError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f'[{x}]- {usn} Người dùng tham gia quá nhiều group!')
                                except UserIdInvalidError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f"[{x}]- {usn} ID đối tượng không hợp lệ cho người dùng")
                                except UserNotMutualContactError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f"[{x}]- {usn} The provided user is not a mutual contact")
                                
                                except UserAlreadyParticipantError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f'[{x}]- {usn} Người Dùng Đã Ở Trong Nhóm')
                                except UserKickedError:
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    print(f'[{x}]- {usn} Người Dùng Đã bị kick')
                                except ValueError:
                                    print(f'[{x}]- Lỗi group kéo mem')
                                    client.disconnect()
                                    exit()
                                except TypeError:
                                    print(f'[{x}]- {usn} Type error')   
                                except ChatAdminRequiredError:
                                    print(f'[{x}]- {usn } Cần Thêm Quyền Quản Trị Trò Chuyện')
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                    #z=z+1
                                except BotGroupsBlockedError:
                                    print(f"[!]-[{usn}] Không kéo đc bot!")
                                    fs = open("id_"+gr+".txt",'a')
                                    fs.write(id+"\n")
                                    fs.close()
                                x=x+1
                    except UserBannedInChannelError:
                        print(f'[!]- Cấm Nhắn Tin Trong Nhóm')
                        lst_phone.remove(phone)
                    except FloodWaitError as e:
                        lst_phone.remove(phone)
                        print(f"[!]- {e}")
                    except UsersTooMuchError:
                        print(f'[i]- Không tham gia được nhóm private!')
                    except PeerFloodError:
                        print(f'[i]- Acc đã bị đánh dấu spam!')
                        lst_phone.remove(phone)
                    except ChatWriteForbiddenError:
                        print(f'[!]- You can\'t write in this chat')
                        #lst_phone.remove(phone)
                    except ChannelsTooMuchError:
                        print("[!]- Account tham gia quá nhiều group")
                        lst_phone.remove(phone)
                    except ChannelPrivateError:
                        print(f"[!]-Không có quyền truy cập kênh!")
                    except KeyboardInterrupt:
                        print(f' ---- Thêm Thành Viên Đã Dùng ----')
                        client.disconnect()
                        exit()
                    except InviteHashExpiredError:
                        print(f"[!]- Không join đc nhóm!")
                        z=z+1
                    except Exception as e:
                        #lst_phone.remove(phone)
                        print(f"[!]-{phone}- {e}")
                    client.disconnect()
            except sqlite3.OperationalError:
                print(f"[!]- Database looked!")
                lst_phone.remove(phone)
            except AuthKeyDuplicatedError:
                print(f"[{x}]-- Session lỗi IP")
                lst_phone.remove(phone)
            except Exception as e:
                client.disconnect()
                print(f"[!]- {e}")
                #lst_phone.remove(phone)
print("                •╔═════☩══♛══☩═════╗•")
print("                    ◆ NGHIAPLUS ◆")
print("                •╚═════☩══✦══☩═════╝•")
print('▬🌺🌺▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🌺🌺▬')
def banner():
    print("\n               Telegram: "+infor)
    print("               Group: "+infor1)
    #print("Donate MOMO: "+ltc)
    print("\n              KÉO MEM TELEGRAM")
    print("                                       Verison: Dùng thử")
    print(f"Notification: {note}\n")

url = "https://pastebin.com/raw/zL2mtXwW"
def get(link):
    req = requests.get(link)
    js = req.json()
    return js
js = get(url)
infor = js["infor"]
infor1 = js['infor1']
note = js['notication']
customer = js['customer']
banner()
sl = input("1 : Tạo session\n2 : Kéo mem\nChọn: ")
if sl == '1':
    if not os.path.exists("session") :
        os.makedirs("session")
    AddMem().cr_session()
else:
    if not os.path.exists("session") or not os.path.exists("list.txt"):
        try:
            os.makedirs("session")
        except FileExistsError:
            pass
        print("Vui lòng tạo session trước, Hoặc nhắn tin @nghialus để được hỗ trợ")
        f = open('list.txt','a')
        f.close()
        exit()
    lst_phone = []
    with open('list.txt',"r") as phones:
        for phone in phones:
            phone = phone.strip()
            lst_phone.append(phone)
    if not os.listdir('session') or lst_phone == []:
        print(lst_phone)
        print("Vui lòng thêm session vào thư mục session và số điện thoại vào list.txt")
        exit()
    if customer == 'True':
    
        gr = input("Group cần thêm mem: ")
        if '@' in gr:
            gr = gr.replace("@","")
        elif "https://t.me/" in gr:
            gr = gr.replace("https://t.me/","")
        fs = open("id_"+gr+".txt",'a')
        fs.close()
        channel = input("Username group lấy mem: ")
        lm = int(input("Giới hạn kéo mỗi acc: "))
        i = int(input("Delay: "))
        AddMem().main()
    else:
        print("Lỗi, liên hệ @nghiaplus để update!")
        exit()
