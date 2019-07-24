import socket
import re

url_str = input('Enter URL : ')
if not re.search('http[s]?://[^ /]+/?\S*',url_str) :
    print('URL wrong format')
    quit()

site = re.findall('http[s]?://([^ /]+)/?\S*',url_str)[0]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    mysock.connect((site, 80))
except :
    print('Socket failed, URL : ',url_str)
    quit()

cmd = ('GET '+url_str+' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()