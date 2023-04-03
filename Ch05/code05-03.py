score = float(input("점수 입력 : "))
absence = int(input("결석 횟수 입력 : "))

if score < 60 or absence >= 4:
    print("F 학점입니다.")
