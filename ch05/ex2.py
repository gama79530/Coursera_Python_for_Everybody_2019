min = None
max = None
total = 0
count = 0
while True :
    try:
        inp = input('Enter a number:')
        if inp == 'done' :
            break
        total += int(inp)
        count += 1
        if min is None or int(inp) < min:
            min = int(inp)
        if max is None or int(inp) > min:
            max = int(inp)
    except :
        print('Invalid input')
print(total,count,min,max)