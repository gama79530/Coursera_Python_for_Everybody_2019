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
print(d)

try :
    fhand.close()
except :
    pass