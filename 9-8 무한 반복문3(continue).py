marks = [90, 60, 67 ,25 ,80]

number = 0
for i in marks:
    number = number + 1
    if i<60: #60보다 작으면 실행
        continue #뒤의 문장 무시하고 조건문 앞에서 부터 다시 시작
    print('%d번 학생 축하합니다. 합격입니다.' %number)
