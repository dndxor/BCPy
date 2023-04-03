charge = 0      #청구 금액
inkum = 0       #받은 금액
outkum = 0      #거스름 금액
payment = 0     #결제방법(현금이면 1, 아니면 0)
cardstatus = 0  #카드상태(정상이면 1, 아니면 0)

charge = int(input("청구 금액(원): "))

while True:
    payment = int(input("결제방법(현금이면 1, 아니면 0)?: "))
    if payment:
        inkum = int(input("받은 금액(원): "))
        outkum = inkum - charge
        if outkum < 0:
            print("금액 부족!")
            continue
        if outkum >= 0:
            print(outkum, "원 반환")
            print("감사합니다.")
            break
    if not payment:
        cardstatus = int(input("카드상태(정상이면 1, 아니면 0)?: "))
        if not cardstatus:
            continue
        if cardstatus:
            print("감사합니다.")
            break