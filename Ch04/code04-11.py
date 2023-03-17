money = int(input("원 단위로 액수를 입력하세요. : "))   #가진 돈의 액수
pencil = 400                                           #연필 가격
print("연필 갯수: %d 자루" % (money // pencil))        #연필 개수 계산 후 출력
print("거스름돈 : %d 원" % (money % pencil))           #거스름돈 계산 후 출력
