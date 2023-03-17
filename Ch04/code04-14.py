grade1 = float(input("1학기 학점 입력 : "))
grade2 = float(input("2학기 학점 입력 : "))
time = int(input("봉사시간 입력 : "))

average = (grade1 + grade2) / 2                 # 학점 평균 구하기
result = (average >= 3.0) and (time >= 10)     # 장학금 대상인지 검사하기
print("장학금 대상 여부 = ", result)              # 결과 출력하기

