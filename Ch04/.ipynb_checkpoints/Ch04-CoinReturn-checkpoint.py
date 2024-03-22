while True :
    totwon = int(input("청구한 금액 입력(원)? "))
    inwon = int(input("받은 금액 입력(원)? "))

    outwon = inwon - totwon    ##거스를 금액
    print("거스름 총 금액 : %d" %outwon)

    coin = outwon // 50000
    outwon %= 50000
    if coin > 0: print("5만원권 %d매" %coin)

    coin = outwon // 10000
    outwon %= 10000
    if coin > 0: print("1만원권 %d매" %coin)

    coin = outwon // 5000
    outwon %= 5000
    if coin > 0: print("5천원권 %d매" %coin)

    coin = outwon // 1000
    outwon %= 1000
    if coin > 0: print("1천원권 %d매" %coin)

    coin = outwon // 500
    outwon %= 500
    if coin > 0: print("5백원동전 %d개" %coin)

    coin = outwon // 100
    outwon %= 100
    if coin > 0: print("1백원동전 %d개" %coin)

    coin = outwon // 50
    outwon %= 50
    if coin > 0: print("50원동전 %d개" %coin)

    coin = outwon // 10
    outwon %= 10
    if coin > 0: print("10원동전 %d개" %coin)

    if coin > 0: print("1원동전 %d개" %outwon)

    print("\n")

