fname = input('Enter file:')
try :
    fhand = open('ch08\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()
count = 0

for line in fhand :
    if not line.startswith('From ') :
        continue
    count += 1
    word = line.split()
    print(word[1])
print('There were %d lines in the file with From as the first word' % count)

try :
    fhand.close()
except :
    pass