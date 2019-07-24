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
    time = words[5].split(':')
    d[ time[0] ] = d.get(time[0] , 0) + 1
t = list(d.items())
if len(t) > 0 :
    t.sort()
for key,val in t :
    print(key,val)

try :
    fhand.close()
except :
    pass