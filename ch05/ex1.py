total = 0
count = 0
while True :
    try :
        inp = input('Enter a number:')
        if inp == 'done' :
            break
        total += int(inp)
        count += 1
    except :
        print('Invalid input')
average = total / count
print(total,count,average)