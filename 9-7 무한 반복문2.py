coffee = 3
while True:
    money = int(input('돈을 넣어주세요'))

    if money == 300:
        coffee=coffee-1
        print('거스름돈 총 0원과 같이  커피를 줍니다. 남은 커피의 양 : %d' %coffee)


    elif money > 300:
        coffee=coffee-1
        print('거스름돈 총 %d원과 같이 커피를 줍니다. ' %(money-300))


    else:
        print('잔액이 부족합니다. 잔액을 더 넣어 주세요. 남은 커피의 양 : %d' %coffee)

    if not coffee:
        print('남은 커피의 양 : %d, 판매를 중지합니다. 관리자에게 문의하세요.' %coffee)
        break # 가장 포큰 범위의 조건문 탈
