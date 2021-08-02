import turtle, random
t=turtle.Turtle()

def f_circle(radius,move_len): #radius : 반지름, move_len 원을 그린 뒤 움직이는 정도
    r=random.random()       #rgb 값을 무작위로 호출
    g=random.random()
    b=random.random()
    t.penup()                   #펜을 들고 move_len 만큼 움직인 후, 펜을 내림
    t.forward(move_len)
    t.pendown()
    t.color(r,g,b)      #무작위로 지정한 rgb를 사용
    t.begin_fill()
    t.circle(radius)    #반지름 만큼 원을 채움
    t.end_fill()

f_circle(100,0)     #원점에서 0만큼 이동한 점을 기준으로 반지름이 100인 원
f_circle(50,100)    #원점에서 100만큼 이동한 점을 기준으로 반지름이 50인 원
f_circle(30,50)     #원점에서 100만큼 이동한 점에서 50만큼 더 이동한 점을 기준으로 반지름이 30인 원
