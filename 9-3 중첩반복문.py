x,y,z=map(int,input('입력 = ').split())

for i in range(x,y,z):
    for j in range(x,y+1,z):
        print('for j in range(x,y+1,z)\ti= ', i, 'j= ',j,'x= ',x,'y= ',y,'z= ',z)
    
