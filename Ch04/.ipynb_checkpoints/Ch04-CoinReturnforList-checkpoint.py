unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]  #List형 데이터 구조
while True :
    totwon = int(input("청구한 금액 입력(원)? "))
    inwon = int(input("받은 금액 입력(원)? "))

    outwon = inwon - totwon    ##거스를 금액
    print("거스름 총 금액 : %d" %outwon)

    for x in unit:
        coin = outwon // x
        outwon %= x
        if coin > 0: print("%d원권 %d개" %(x, coin))
    print()

