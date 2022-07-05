import requests,smtplib,os,time
from email.mime.text import MIMEText

from requests.api import get
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def ms(rec) : #用yubantech@qq.com发警告邮件给rec
    mail_host = 'smtp.qq.com'  
    mail_user = 'yubantech@qq.com'  
    mail_pass = 'nydzpprkkquobadi'   
    sender = 'yubantech@qq.com'  
    receivers = [rec]  

    message = MIMEText('警告：御坂网络MC服务出现异常，无法修复，请立即前来检查！！','plain','utf-8')      
    message['Subject'] = '御坂网络MC服务出现异常' 
    message['From'] = sender 
    message['To'] = receivers[0]  

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(sender,receivers,message.as_string()) 
        smtpObj.quit() 
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        requests.get('https://api.day.app/d6VGa63bqyKJW5VgVRXHoe/哈哈哈你妈的服务炸啦！/快维修吧！frp和邮件都炸啦?url=http://ssh.unreve.top:23333&level=timeSensitive')

def sd(status): #如果无法修复则输入True
    if status == True :
        ms('yubantech@qq.com')
        #ms('qq18929261343@gmail.com')
        requests.get('http://192.168.2.41:54870/sendMessage?t=Group&n=322819699&m=御坂网络MC服务出现无法修复的问题！请及时检修')
        requests.get('https://api.day.app/d6VGa63bqyKJW5VgVRXHoe/哈哈哈御坂网络MC服务致命错误！/无法修复，点击这里给老子爬去检查?url=http://ssh.unreve.top:23333&level=timeSensitive') 
    else :
        requests.get('http://192.168.2.41:54870/sendMessage?t=Group&n=322819699&m=御坂网络MC服务出现问题！正在尝试修复，请等待30秒...')

def zaima() : #检查网站是否在线
    requests.keep_alive = False
    a = 0
    for i in range(5) :
        z = requests.get('http://blog.yuban.tech/test1145141919810aaaaaaaaa',headers=headers,timeout=4)
        a = z.status_code
        if a==200 : 
            break
        time.sleep(1)
    return a

print('现在时间是'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' ，webcheck程序已经启动！')
# 开始循环
while 1:
    ti=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" "
    za=zaima()
    if (za==503):
        print(ti+'frpc断线，正在重启服务')
        sd(False)
#        os.system ('systemctl restart frpc@n9bzcly6xoyhqeg466kkwb6we5pm68hz:3546869.service')
        requests.get("http://192.168.2.41:54868/refrp")
        time.sleep(30)
        za=zaima()
        if(za!=200):
            sd(True)
            input(ti+'FRP无法修复，程序暂停运行。请按回车继续检测')
            print(ti+'检测程序继续运行')
        else :
            print(ti+'服务已修复成功')
            requests.get('http://192.168.2.41:54870/sendMessage?t=Group&n=322819699&m=MC服务已修复')

    elif (za!=200):
        sd(True)
        input(ti+'遇到不可修复的异常，程序暂停运行。请按回车继续检测')
        print(ti+'检测程序继续运行')
    else :
        print(ti+'FRP测试成功')
    time.sleep(60)
