number = int(input("주민번호 뒷부분 한 자리 숫자를 입력하세요 : "))

if 1 <= number <= 4 :
    if number % 2 == 1 :    # 2로 나눈 나머지가 1인 경우(= 1 또는 3)
        print("회원은 남자입니다.")
    else :
        print("회원은 여자입니다.")
else :       # 잘못된 입력인 경우
    print("올바른 값이 아닙니다!")
