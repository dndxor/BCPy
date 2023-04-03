money = int(input("환전하려는 금액(원) : "))
nation = input("국가 선택(미국/영국/러시아/중국) : ")

exchange = 0; currency = ""

if nation == "미국":
    exchange = money / 1188.50
    currency = "달러"
elif nation == "영국":
    exchange = money / 1570.13
    currency = "파운드"
elif nation == "러시아":
    exchange = money / 15.01
    currency = "루블"
elif nation == "중국":
    exchange = money / 173.93
    currency = "위안"
else:
    print("국가를 잘못 입력했습니다.")
    
print("%.2f" % exchange, currency) #소수점 이하 2자리로 단위도 함께 출력 
