x,y,z = map(int,input('x,y,z 값 입력').split())
for i in range(x,y,z):
    print('for i in range(x,y,z):',i,'\tx',x,'y',y,'z',z)

import random
while z>=0: # z가 양수 및 0일 때만 작동!
    f = random.randint(x,y)
    z=z-1
    print('\n','='*10,'\n',f)

for b in ['H','e','l','l','o']:
    print(b)

 # z>0이면 range(x,y,z) x~(y-1)까지의 값을 z 간격으로 출력 (단, x<=y)
 # z<=0이면 range(x,y,z) x~(y+1)까지의 값을 z 간격으로 출력(단, x>=y)

# import random
# a= random.randint(x,y) x~!!!!"y"!!!! 사이의 임의의 정수 값을 불러옴.
# for 문의 range()에는 종료 값만 표기 가능!! (시작값은 0으로, 증감값은 1로 고종)
