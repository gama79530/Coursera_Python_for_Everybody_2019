fname = input('Enter the file name:')
try :
    fhand = open('ch09\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()

d = {}
for line in fhand :
    if not line.startswith('From ') :
        continue

    words = line.split()
    d[ words[1] ] = d.get(words[1] , 0) + 1

max_num = 0
max_man = ''
for man in d :
    if d[man] > max_num :
        max_man = man
        max_num = d[man]
print(max_man,max_num)

try :
    fhand.close()
except :
    pass