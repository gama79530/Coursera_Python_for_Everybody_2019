fname = input('Enter the file name:')
try :
    fhand = open('ch10\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()

d = {}
for line in fhand :
    line = line.lower()
    for c in line :
        if 'a' <= c and c <= 'z' :
            d[c] = d.get(c,0) + 1
total = sum(d.values())
for key in d :
    d[key] /= total
t = list(d.items())
t.sort()
for key,val in t :
    print(key,'%.2f'%(val*100) + '%' )

try :
    fhand.close()
except :
    pass