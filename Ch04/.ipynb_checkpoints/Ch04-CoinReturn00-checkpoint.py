totwon = 0
inwon = 0
outwon = 0

while True :
    totwon = int(input("청구한 금액 입력(원)? "))
    inwon = int(input("받은 금액 입력(원)? "))

    outwon = inwon - totwon    ##거스를 금액
    print("거스름 총 금액 : %d" %outwon)


