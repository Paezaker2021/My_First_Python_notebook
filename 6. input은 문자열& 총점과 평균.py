a= input("a: ")
b= input("b: ")
print(a+b)

#input으로 받은 값은 숫자(int)가 아니라 문자(char) 형태로 가져오기 때문에, 숫자를 연산하는 것이 아니라, 문자를 그냥 붙여준 것임.
#input 을 int(input)으로 변경해야만 문자 형태가 아닌 숫자로 받아옴!

kor=int(input("국어: ")):
eng=int(input("영어: ")):
math=int(input("수학: ")):
total=kor+eng+math
print("총점: ",total,"평균 :",total/3)

