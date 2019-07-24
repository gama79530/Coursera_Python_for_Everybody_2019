fname = input('Enter the file name:')
try :
    fhand = open('ch10\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()

d = {}
for line in fhand :
    if not line.startswith('From ') :
        continue

    words = line.split()
    d[ words[1] ] = d.get(words[1] , 0) + 1
t = []
for key,val in d.items() :
    t.append((val,key))
if len(t) > 0 :
    t.sort(reverse=True)
    (val,key) = t[0]
    print(key,val)

try :
    fhand.close()
except :
    pass