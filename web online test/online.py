import requests,os,time
token = 'n9bzcly6xoyhqeg466kkwb6we5pm68hz'
id = '3546869'
def gt(tk,d):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    'Connection': 'close'
    }
    try:
        url = 'https://api.natfrp.com/v1/tunnel/get?token={}&id={}'.format(tk,d)
        r=requests.get(url,headers=headers)
        if (r.status_code==200):
            return r.json()
        else:
            print ('Error Code:'+ r.status_code)
            return 599
    except  Exception as e:
        return 599

def ti():
    i=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' '
    return i

#200 正常
#0 连接出错
#400 不在线
#-1 中止运行
def check():
    re=gt(token,id)
    if (re != 599):
        if (re.get('success',True)==False):
            print(ti()+'返回出错：'+ re.get('message','暂无返回内容'))
            return -1
        elif(re.get('online')==True) :
            print(ti()+'御坂网络MC：frp服务正常在线中')
            return 200
        else:
            print(ti()+'御坂网络MC：frp隧道不在线，正在尝试重启')
            return 400  
    else :
        print(ti()+'连接出错，将在一分钟后重试')
        return 0

#主函数
while 1:
    s=check()
    if(s==-1): break
    if(s==400):
        os.system ('systemctl restart frpc@n9bzcly6xoyhqeg466kkwb6we5pm68hz:3546869.service')
        print(ti()+'重启完成，30秒后将再次检测...') 
        time.sleep(30)
        s=check()
        if(s==400):
            requests.get('http://192.168.2.41:54870/sendMessage?t=Group&n=322819699&msg=御坂网络MC：frp服务遇到无法修复的错误，请速来检修')
            requests.get('https://api.day.app/d6VGa63bqyKJW5VgVRXHoe/哈哈哈御坂网络MC服务致命错误！/无法修复，点击这里给老子爬去检查?url=http://ssh.unreve.top:23333&level=timeSensitive')
            input(ti()+'遇到不可修复的异常，程序暂停运行。请按回车继续检测')
        else:
            print(ti()+'frp已修复')
    time.sleep(60)
print(ti()+'程序结束，请检查请求地址与token、id')
