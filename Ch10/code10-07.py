#환율 계산기(함수와 딕셔너리)

def calc_money(n, m) :       # 함수 정의
    moneyInfo = {"미국":(1188.50, "달러"), "영국":(1570.13, "파운드"),
                 "러시아":(15.01, "루블"), "중국":(173.93, "위안")}
    if n in moneyInfo:
        rate, unit = moneyInfo.get(n)   # 검색한 값(튜플)을 두 변수에 나누어 담기
        print("%d(원)을 %.2f(%s)로 교환합니다." % (m, m/rate, unit))
    else :
        print("국가를 잘못 입력했습니다.")
    
money = 0 #금액
nation = 0 #국가

try:
    money = int(input("환전하려는 금액(원) : "))
except:
    print("금액은 숫자로 입력하세요.")    
else:
    nation = input("국가(미국/영국/러시아/중국) : ")
    calc_money(nation, money)       # 함수 호출 
    
