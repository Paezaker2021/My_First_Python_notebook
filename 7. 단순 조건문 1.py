kor=int(input("국어: "))
eng=int(input("영어: "))
math=int(input("수학: "))
total=kor+eng+math
print('='*15)
print('총점=',total)
score=round(total/3.0)  #반올림?
print('평균=',score)
print('='*15)


if total: #아무 조건이 없으면 부울형에 의해 0이 아닌 모든 실수에 대해 참이 나옴. 즉 0이 아니면 무조건 실행됨
    print("수고")

print('했습니다')

