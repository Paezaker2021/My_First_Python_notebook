import turtle
t=turtle.Turtle()

def f():    #파란색 줄을 긋고 커서를 왼쪽으로 60도 돌리기
    t.color("blue")
    t.forward(100)
    t.left(60)

def h():    #함수 f를 6번 실행하기 → 육각형이 만들어지고, 커서는 시작한 위치에 감.
    f(),f(),f(),f(),f(),f()

def g():    #육각형이 만들어지고, 처음 만들어진 변의 색깔을 파란색에서 붉은 색으로 변경 후, 커서를 오른쪽으로 60도로 돌림
    h()
    t.color("red")
    t.forward(100)
    t.right(60)

g(),g(),g(),g(),g(),g()     #바깥에는 6개가 만들어지지만, 안쪽에 1개가 더 생김
