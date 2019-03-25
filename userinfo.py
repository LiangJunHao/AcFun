import os
import requests
from fake_useragent import UserAgent #fake_useragent
import threading  #多线程
import time   #记录运行时间
import middle

def download(a,b,c):
    start=time.time()
    middle.mkdir(os.curdir+'\\userinfo\\'+str(a))
    current_position = str(os.getcwd()) + '\\userinfo\\' + str(a) + r'\current.txt'
    for i in range(a,b):
        url = 'http://www.acfun.cn/usercard.aspx?uid=' + str(i)
        print(url)
        #currentD = str(os.getcwd()) + r'\user\acfun_usercard_uid=' + str(i) + '.json'
        ua = UserAgent()
        #user_agent = random.choice(USER_AGENTS)
        #headers = {'User-Agent': user_agent}
        #req = urllib.request.Request(url,headers=headers)
        headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                   'Accept - Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                   'Connection': 'Keep-Alive',
                   'User-Agent':ua.random}

        try:
            # urllib.request.urlretrieve(req,currentD)  #不改header直接下载
            r = requests.get(url, headers=headers, timeout=3)
            current_position = str(os.getcwd()) + '\\userinfo\\' + str(a) + r'\current.txt'
            middle.write_to_file(current_position,'w',str(i))
            #current_position = open(str(os.getcwd()) + '\\testuser\\'+str(a)+r'\current.txt', 'w')#记录当前下载位置
            #current_position.write(str(i))
            #current_position.close()#关闭文件
            if (r.status_code!=200):#非正常
                print("error!status code:"+str(r.status_code))
                status_code_error = str(os.getcwd()) + '\\userinfo\\'+str(a)+r'\user_info_log.txt'
                middle.write_to_file(status_code_error,'a','user ' + str(i) + ':status code =' + str(r.status_code)+'\n')
                #f = open(str(os.getcwd()) + '\\testuser\\'+str(a)+r'\user_info_log.txt', 'a', encoding='utf-8')  #状态码
                #f.write('user ' + str(i) + ':status code =' + str(r.status_code)+'\n')
                #f.close
            #print(r.apparent_encoding)
            print("Thread:"+str(c))



            #f1=open(str(os.getcwd())+r'\userinfo\user_information_'+str(i)+'.html','w')
            f1 = open(str(os.getcwd()) + r'\userinfo\\'+str(a)+r'\user_info_' + str(i) + '.html', 'w') #test
            for line in r.text: #写入文件
                f1.writelines(line)
            f1.close()

        except:
            print("fail to get the site")
            f = open('log.txt','a',encoding='utf-8')
            f.write('user '+str(i)+':Wrong with site.\n')
            f.close()
    end = time.time()
    cost=end-start
    #current_position = open(str(os.getcwd()) + '\\testuser\\' + str(a) + r'\current.txt', 'a')  # 记录当前下载位置
    #current_position.write("Done\n"+'time='+str(cost)+'seconds')
    #current_position.close()  # 关闭文件
    middle.write_to_file(current_position,'a',"\nDone\n"+'time='+str(cost)+' seconds')


            #os.rename(os.getcwd()+r'\user\acfun_usercard_uid='+str(i)+'.json',os.getcwd()+r'\user\acfun_usercard_uid='+str(i)+'.json'+'(error)')
            #if(os.path.isfile('http://www.acfun.cn/usercard.aspx?uid='+str(i))):


#threads=[]
#test for a little amount of users
t1 = threading.Thread(target=download,args=(1,100,'1'))
t2 = threading.Thread(target=download,args=(100,200,'2'))
t3 = threading.Thread(target=download,args=(200,300,'3'))
t4 = threading.Thread(target=download,args=(300,400,'4'))
t5 = threading.Thread(target=download,args=(400,500,'5'))
#t6 = threading.Thread(target=download,args=(50001,60000,'Thread6'))
#threads.append(t1)
#threads.append(t2)

if __name__ == '__main__':
    try:
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        #t6.start()
        
    except:
        print("error starting thread")


