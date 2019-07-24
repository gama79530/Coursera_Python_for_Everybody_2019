d = {}
fhand = open('ch09\\words.txt')

for line in fhand :
    words = line.split()
    for word in words :
        d[word] = 'values - ' + word
    
inp = input('Enter a word :')
if inp in line :
    print('\''+inp+'\' is in dictionary.')
else :
    print('\''+inp+'\' is not in dictionary.')