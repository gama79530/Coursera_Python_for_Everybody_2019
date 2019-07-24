try :
    hour = float(input('Enter Hours:'))
    rate = float(input('Enter Rate:'))
except :
    print('Error, please enter numeric input')
    quit()

pay = None
if hour <= 40 :
    pay = hour * rate
else :
    pay = 40 * rate + (hour - 40) * 1.5 * rate

print('Pay:',pay)