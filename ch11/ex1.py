import re
reg_exp = input('Enter a regular expression:')
fhand = open('ch11\\mbox.txt')
c = 0
for line in fhand :
    if re.search(reg_exp,line) :
        c += 1
print('mbox.txt had %d lines that matched %s' % (c,reg_exp))

fhand.close()