def grade(score) :
    if score > 1 or score < 0:
        print('Bad score')
    elif score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    else :
        print('F')

score = None
try :
    score = float(input('Enter score:'))
    grade(score)
except:
    print('Bad score')
    quit()