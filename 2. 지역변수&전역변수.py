a=10     #전역변수
b=20
print('a+b=',a+b)


def 곱():
    global c
    c=a*b       #Global이 없으면 지역 / 있으면 전역 변수로 사용됨
    print('c=',c)


def 합():
    print('c+a=',c+a)       #Global이 없으면 c값이 지정되지 않음.


곱()
합()
