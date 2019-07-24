import urllib.request,urllib.parse,urllib.error
import re

url_str = input('Enter URL : ')
if not re.search('http[s]?://[^ /]+/?\S*',url_str) :
    print('URL wrong format')
    quit()

try :
    uhand = urllib.request.urlopen(url_str)
except :
    print('Invalid URL')
    quit()

count = 0
for line in uhand :
    if count + len(line) <= 3000 :
        print(line.decode(),end='')
    elif count < 3000 :
        str = line.decode()
        remain_len = 3000-count
        print(str[ : remain_len])
        print('Length exceed 3000.')
    count += len(line)
print(count)