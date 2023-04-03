height = int(input("키 입력(cm) : "))
weight = int(input("몸무게 입력(kg) : "))

bmi = weight / (height / 100) ** 2  # 키를 미터 단위로 변환한 후 계산
print("*** 체질량지수 %.1f :" % bmi, end=' ')  # 소수점 이하 1자리로 출력
'''
##복잡도 : 20/4=5.0
if bmi < 18.5 :
    print("저체중, 건강 위험도 높음 ***")
if bmi >= 18.5 and bmi < 25 :
    print("정상체중, 건강 위험도 낮음 ***")
if bmi >= 25.0 and bmi < 30 :
    print("과체중, 건강 위험도 낮음 ***")
if bmi >= 30 :
    print("비만, 건강 위험도 높음 ***")

##복잡도 : 9/4=2.25
if bmi >= 18.5 :
    if bmi < 25 :
        print("정상체중, 건강 위험도 낮음 ***")
    else :
        if bmi < 30 :
            print("과체중, 건강 위험도 낮음 ***")
        else :
            print("비만, 건강 위험도 높음 ***")
else :
    print("저체중, 건강 위험도 높음 ***")

##복잡도 : 9/4=2.25
if bmi < 18.5 :
    print("저체중, 건강 위험도 높음 ***")
elif bmi < 25 :
    print("정상체중, 건강 위험도 낮음 ***")
elif bmi < 30 :
    print("과체중, 건강 위험도 낮음 ***")
else :
    print("비만, 건강 위험도 높음 ***")
'''
##복잡도 : 8/4=2.0
if bmi < 25 :   # 저체중이거나 정상체중인 경우
    if bmi < 18.5 :
        print("저체중, 건강 위험도 높음 ***")
    else :
        print("정상체중, 건강 위험도 낮음 ***")
else :          # 과체중이거나 비만인 경우
    if bmi < 30 :
        print("과체중, 건강 위험도 낮음 ***")
    else :
        print("비만, 건강 위험도 높음 ***")

input("In: ")