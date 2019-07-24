fname = input('Enter a file name:')
try :
    fhand = open('ch07\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()
for str in fhand :
    print(str.upper().rstrip())
try :
    fhand.close()
except :
    pass