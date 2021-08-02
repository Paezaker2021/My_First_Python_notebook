kor=int(input("국어: "))
eng=int(input("영어: "))
math=int(input("수학: "))
total=kor+eng+math
print('='*15)
print('총점=',total)
score=round(total/3.0)
print('평균=',score)
print('='*15)

if score>=70:
    print('PASS')

    if score==100:
        print('PERFECT')

elif score>=50:
    print('SUB PASS')

else:
    print('FAIL')

    if score==0:
        print('WTF')


