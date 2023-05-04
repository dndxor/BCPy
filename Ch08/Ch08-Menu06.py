## [실습] 카페 메뉴표를 딕셔너리로 구성하기 (계속 주문 처리)
#(소분류) 메뉴표 만들기
menu = {'COFFEE': [['에스프레소', 3.0], ['아메리카노', 3.0], ['카페라떼', 4.0], ['카프치노', 4.0]],
          'LATTE': [['말차라떼', 4.0], ['초코라떼', 4.0], ['카페라떼', 4.0]],
          'TEA': [['청귤차', 4.0], ['자몽차', 4.0], ['레몬차', 4.0], ['카모마일', 4.5]],
          'ADE': [['자몽에이드', 4.5], ['레몬에이드', 4.5], ['청포도에이드', 4.5]],
          'JUICE': [['망고', 4.5], ['바나나', 4.5], ['딸기', 4.5], ['키위', 4.5]],
          'SMOOTHIE': [['청귤스무디', 4.5], ['요거트스무디', 4.5]],
          'MILK TEA': [['흑당밀크티', 4.5], ['달고나밀크티', 4.5]]}

#[주문] 대분류 메뉴 선택
print("\n>> [선택] 대분류 메뉴 <<")
for no, title in menugroup.items():
    print("[%d] %s" %(no, title))  #대분류 메뉴 출력

mcnt = len(menugroup)
nogroup = -1
while nogroup < 0 or nogroup >= mcnt:
    print('-'*30)
    nogroup = int(input(">>메뉴 그룹(번호) 선택: "))
inkey = menugroup.get(nogroup)    #소분류 메뉴(menu) 키 찾기
mlist = menu.get(inkey)	   # 소분류 메뉴(menu) 키로 소분류 메뉴 리스트 구성(찾기)
print(mlist)		 # 소분류 메뉴 출력

#[주문] 소분류 메뉴 선택
print("\n>> [%s] 소분류 메뉴 <<" %inkey)
seq = 0
for mmenu, price in mlist:	#선택 메뉴 출력
    print("[%d] %-10s\t%5.1f" %(seq, mmenu, price))
    seq += 1   	#순서번호 생성

mcnt = len(mlist)	#선택 가능한 메뉴 수
nomenu = -1	#메뉴 선택번호
while nomenu < 0 or nomenu >= mcnt:
    print('-'*30)
    nomenu = int(input(">>메뉴(번호) 선택: "))
print("> %s를 선택하셨습니다." %mlist[nomenu][0])

selmlist = []    #주문내역 리스트 생성
#[주문] 주문내역 리스트 생성
inqty = 0	#주문 수량
while inqty <= 0:
    inqty = int(input(">>몇 잔을 원하십니까? "))
print("> [%s]를 [%d]잔 선택하셨습니다." %(mlist[nomenu][0], inqty))
totprice = int(mlist[nomenu][1]*inqty*1000)    #주문내역 리스트에 추가
selmlist.append([mlist[nomenu][0], mlist[nomenu][1], inqty, totprice])
print(selmlist)

insel = input(">>계속 주문을 하시겠습니까? [종료: x, 계속: Enter] ")
if insel == 'x' or insel == 'X':
    break
