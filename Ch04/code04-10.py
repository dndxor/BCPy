n = int(input("3에서 6 사이의 정수를 입력하세요 : "))    #다각형 모양 선택
sumAngle = 180 * (n - 2)        #내각의 합 계산
intAngle = 180 * (n - 2) / n    #한 내각의 크기
print("정%d각형의 내각의 합 = %d도" % (n, sumAngle))
print("정%d각형의 한 내각의 크기 = %d도" % (n, intAngle))
