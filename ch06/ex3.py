def count( word , letter ) :
    c = 0
    for l in word :
        if l == letter :
            c += 1
    return c

word = input('Enter a string:')
letter = input('Enter a test letter:')
print( count( word , letter ) )