menu = int(input("번호 입력(1:온도, 2:무게, 3:길이) : "))
value = float(input("변환할 값 입력 : "))

if menu == 1 :      # 온도 단위 변환
    print("변환 결과 = %.2f ℃" % ((value - 32) / 1.8)) 
elif menu == 2 :    # 무게 단위 변환
    print("변환 결과 = %.2f ㎏" % (value * 0.453592)) 
elif menu == 3 :    # 길이 단위 변환
    print("변환 결과 = %.2f ㎝" % (value * 2.54)) 
else :              # 잘못된 메뉴 선택
    print("메뉴 선택 오류!")
