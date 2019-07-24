fname = input('Enter file:')
word_list = []
try :
    fhand = open('ch08\\' + fname)
except :
    print('File cannot be opened:',fname)
    quit()

for read_line in fhand :
    split_line = read_line.split()
    for word in split_line :
        if not word in word_list :
            word_list.append(word)
word_list.sort()
print(word_list)

try :
    fhand.close()
except :
    pass