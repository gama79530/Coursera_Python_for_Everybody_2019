def chop(t) :
    if len(t) > 0 :
        t.pop(0)
    if len(t) > 0 :
        t.pop()

def middle(t) :
    if len(t) > 1 :
        return t[ 1 : len(t)-1 ]
    else :
        return []

x = [ 1 , 2 , 3 , 4 , 5 , 6]
print('x =' , x)
print('chop(x) :' , chop(x))
print('x =' , x)
y = middle(x)
print('y = middle(x) :' , y)
print('x =' , x)
