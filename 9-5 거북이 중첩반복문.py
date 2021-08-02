import turtle
t=turtle.Pen()

i=1
while i<=6:
    j=1
    print('i ====== ',i)
    while j<=4:
        t.forward(60)
        t.right(90)
        print('j = ',j)
        j+=1
    t.left(60)
    i+=1
