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
    address = words[1]
    domain_name = address[ address.find('@')+1 : ]
    d[domain_name] = d.get(domain_name,0) + 1
print(d)

try :
    fhand.close()
except :
    pass