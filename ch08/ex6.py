num_list = []
while True :
    inp = input('Enter a number:')
    if inp == 'done' :
        break
    try :
        num_list.append(float(inp))
    except :
        pass
print('Maximum:',max(num_list))
print('Minimum:',min(num_list))