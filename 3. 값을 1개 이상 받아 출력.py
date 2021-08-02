def 과목(name):
    print("다음 수업은",name,"입니다")

def 운동(a,b):
    print("오늘 줄넘기를",a,"번 했고\n달리기를",b,"번 하였다.")

과목('정보')
운동(200,5)

print('='*10)

def 최댓값(c,d,e):
    print(c,d,e,"중 가장 큰 값은")
    f=max(c,d,e)
    return f


print(최댓값(20,300,999))
