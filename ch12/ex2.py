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

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if count + len(data) <= 3000 :
        print(data.decode(),end='')
    elif count < 3000 :
        str = data.decode()
        remain_len = 3000-count
        print(str[ : remain_len])
        print('Length exceed 3000.')
    count += len(data)
print(count)
mysock.close()