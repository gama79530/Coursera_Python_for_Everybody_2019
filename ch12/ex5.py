import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

is_content = 0 
# 0 -> normal  
# 1 -> end with \r  
# 2 -> end with \r\n
# 3 -> end with \r\n\r
# 4 -> is content
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    str = data.decode()

    if is_content == 4 :
        print(str,end='')
        continue
    elif is_content == 1 and str.startwith('\n\r\n') :
        str = str[ 3: ]
        print(str,end='')
        is_content = 4
        continue
    elif is_content == 2 and str.startwith('\r\n') :
        str = str[ 2: ]
        print(str,end='')
        is_content = 4
        continue
    elif is_content == 3 and str.startwith('\n') :
        str = str[ 1: ]
        print(str,end='')
        is_content = 4
        continue
    
    x = str.find('\r\n\r\n')
    if x > 0 :
        str = str[ (x+4): ]
        print(str,end='')
        is_content = 4
        continue

    str.endswith('\r\n\r')
    if str.endswith('\r\n\r') :
        is_content = 3
    elif str.endswith('\r\n') :
        is_content = 2
    elif str.endswith('\r') :
        is_content = 1
    else:
        is_content = 0

mysock.close()