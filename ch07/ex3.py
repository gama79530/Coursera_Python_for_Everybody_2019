fname = input('Enter the file name:')
try :
    fhand = open('ch07\\' + fname)
except :
    if fname == 'na na boo boo' :
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else :
        print('File cannot be opened:',fname)
    quit()
count = 0
for str in fhand :
    count += 1
print('There were %d subject lines in %s' % (count,fname))
try :
    fhand.close()
except :
    pass