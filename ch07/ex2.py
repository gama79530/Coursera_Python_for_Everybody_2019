fname = input('Enter the file name:')
try :
    fhand = open('ch07\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()
count = 0
conf = 0.
for str in fhand :
    if not str.startswith('X-DSPAM-Confidence:') :
        continue
    count += 1
    conf += float(str.lstrip('X-DSPAM-Confidence: '))
print('Average spam confidence:',conf / count)
try :
    fhand.close()
except :
    pass