## [실습] 카페 메뉴표를 딕셔너리로 구성하기 (대분류 메뉴표 생성)
#(소분류) 메뉴표 만들기
menu = {'COFFEE': [['에스프레소', 3.0], ['아메리카노', 3.0], ['카페라떼', 4.0], ['카프치노', 4.0]],
          'LATTE': [['말차라떼', 4.0], ['초코라떼', 4.0], ['카페라떼', 4.0]],
          'TEA': [['청귤차', 4.0], ['자몽차', 4.0], ['레몬차', 4.0], ['카모마일', 4.5]],
          'ADE': [['자몽에이드', 4.5], ['레몬에이드', 4.5], ['청포도에이드', 4.5]],
          'JUICE': [['망고', 4.5], ['바나나', 4.5], ['딸기', 4.5], ['키위', 4.5]],
          'SMOOTHIE': [['청귤스무디', 4.5], ['요거트스무디', 4.5]],
          'MILK TEA': [['흑당밀크티', 4.5], ['달고나밀크티', 4.5]]}

#대분류 메뉴표 딕셔너리 생성
menugroup = {}
no = 0
for title in menu.keys():
    menugroup[no] = title    #딕셔너리에 항목 추가
    no += 1

#[출력] 대분류 메뉴표 딕셔너리
print("[[ 대분류 메뉴 ]]")
for no, title in menugroup.items():
    print("%d : %-10s" %(no, title))