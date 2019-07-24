import re
fname = input('Enter file:')
try :
    fhand = open('ch11\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()

num_list = []
for line in fhand :
    reg_list = re.findall('^New Revision: ([0-9]+).*',line)
    for num in reg_list :
        num_list.append(int(num))
print( sum(num_list)/len(num_list) )

try :
    fhand.close()
except :
    pass