import flask, ipaddress, requests,os
# 这玩意拿来把DDNS-GO的一个webhook变成俩webhook（同时请求机器人与Apple统一推送）.并且启动这个会自动启动app.py


def A():
    os.system('python3 app.py')

def allow(ip):
    if 2130706433 <= int(ipaddress.IPv4Address(ip)) <= 2147483647 or 3232236032 <= int(ipaddress.IPv4Address(ip)) <= 3232236287:
        return True
    return False

app = flask.Flask(__name__)
@app.route("/DDNS")
def gm():
    if not allow(flask.request.remote_addr):
        flask.abort(403)
    #s:更新状态；i：更新后的IP
    r = '{"code":200,"msg":"OK"}'
    s = flask.request.args.get("s")
    i = flask.request.args.get("i")
    if s is None or i is None:
        flask.abort(400)   
    url1 = 'https://api.day.app/d6VGa63bqyKJW5VgVRXHoe/啊哈哈哈哈IP来咯！/尼的DDNS更新' + s + '，现在的IP是' + i +'！?url=http://ssh.unreve.top:23333&level=timeSensitive'
    url2 = 'http://192.168.2.41:54870/sendMessage?t=Group&n=322819699&m=IP地址发生变化，DDNS' + s
    requests.get(url1)
    requests.get(url2)
    return r
app.run("0.0.0.0", 54869)
