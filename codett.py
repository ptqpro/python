from random import randint
import os,sys,time

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
def lyric():
    
    a="               bởi\n                vì\n                 đằng\n                  sau\n                   luôn\n                    có\n                     anh\n                      nhìn\n                       theo..\n\n"
    lyric="""                 hãy cầm chặt tay anh,\n                    anh sẽ dắt em đi qua nỗi đau này\n                 và dìu em bước\n                    trên con đường dài \n                 phía trước..\n\n                    code by fivex\n"""
    #os.system('clear')
    for i in a:
       sys.stdout.write(green+i)
       sys.stdout.flush()
       time.sleep(0.01)
    #os.system('clear')
    time.sleep(1)
    for l in lyric:
       x=randint(0,7)
       o=[2,3,7,7,3,2]
       #c=o[x]
       color='\033[1;9'+str(x)+'m'
       sys.stdout.write(color+l)
       sys.stdout.flush()
       time.sleep(0.01)
lyric()