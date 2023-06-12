from tkinter import *

menu = {'COFFEE': [['에스프레소', 3.0], ['아메리카노', 3.0], ['카페라떼', 4.0], ['카프치노', 4.0]],
          'LATTE': [['말차라떼', 4.0], ['초코라떼', 4.0], ['카페라떼', 4.0]],
          'TEA': [['청귤차', 4.0], ['자몽차', 4.0], ['레몬차', 4.0], ['카모마일', 4.5]],
          'ADE': [['자몽에이드', 4.5], ['레몬에이드', 4.5], ['청포도에이드', 4.5]],
          'JUICE': [['망고', 4.5], ['바나나', 4.5], ['딸기', 4.5], ['키위', 4.5]],
          'SMOOTHIE': [['청귤스무디', 4.5], ['요거트스무디', 4.5]],
          'MILK_TEA': [['흑당밀크티', 4.5], ['달고나밀크티', 4.5]]}
menugroup = {}  #대분류 메뉴
orders = {}     #주문내역 딕셔너리
oqty = 1        #주문 버튼 선택 시 증가 수량

def new_menugroup():    #대분류 메뉴표 딕셔너리 생성
    no = 0
    for title in menu.keys():
        menugroup[no] = title    #딕셔너리에 항목 추가
        no += 1

def win_text_insert():  #Text박스에 주문내역 갱신 출력
    global orders
    global txt1
    txt1.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
    totqty, totwon = (0, 0)
    seq = 0
    for mmenu, olist in orders.items():
        seq += 1
        price, qty, totprice = olist
        line = "[{0:>2}] {1:<10} {2:>5}  {3:>3}  {4:>8}".format(seq, mmenu, price, qty, totprice)
        txt1.insert(CURRENT, line+'\n')
        totwon += totprice
        totqty += qty
    line = "{}".format("-"*42)
    txt1.insert(CURRENT, line+'\n')
    line = "주문 합계: {0:>16}잔 {1:>10}원".format(totqty, totwon)
    txt1.insert(CURRENT, line+'\n')

def btn_menu(i, j):     #주문 메뉴 orders 딕셔어리에 추가 (i:클릭 버튼 행 번호, j:클릭 버튼 열번호)
    global menu
    mkey = menugroup[j]
    mlist = menu.get(mkey)
    mmenu = mlist[i][0];   price = mlist[i][1];   qty = 1;   totprice = mlist[i][1] * 1000;
    # 주문내역 orders 딕셔너리에 추가
    if mmenu in orders.keys():  #중복되는 주문 메뉴는 수량만 증가 처리
        orderlist = orders.get(mmenu)
        price, qty, totprice = orderlist
        qty += oqty     #=1 or -1로 증가
        totprice = price * 1000 * qty
    if qty == 0:
        del orders[mmenu]
    else:
        orders[mmenu] = [price, qty, totprice]  #주문 메뉴 갱신 또는 추가 처리
    win_text_insert()   #주문 버튼 생성

def set_oqty():     #주문 수정 버튼(toggle 1/-1) 토글 처리
    global oqty
    if oqty == 1:
        oqty = -1   #주문 감소(조정)
        txt1.config(bg="lightpink")
        ebt.config(bg="lightpink", relief="sunken")
    else:
        oqty = 1    #주문 수량
        txt1.config(bg="white")
        ebt.config(bg="white", relief="raised")

############# Main ###############################
new_menugroup()     #menu(소분류) 딕셔너리로부터 menugroup(대분류) 딕셔너리 구성

#기본 윈도우 생성
w = Tk()
w.title("부천대학 컴퓨터소프트웨어과 Dreammer Cafe")      #윈도우 타이틀("제목")
w.geometry("700x500+100+100")     #윈도우 크기 및 기준점("너비x높이+x좌표+y좌표")
w.resizable(1, 1)       #창 크기 조절 가능 여부(상하, 좌우)

#menu 딕셔너리 기반 주문 버튼 생성
ix, iy = (0, 0)
xp, yp = (0, 0)
for menugrp, mlist in menu.items():
    xp = 10;
    yp = iy * 30
    Label(w, text=menugrp, bg="maroon", fg="yellow", relief="ridge").place(x=xp, y=yp, width=100)
    ix = 0
    for mmenu, price in mlist:
        xp = 120 + ix * 140
        menutxt = mmenu + ' ' * int(14 - len(mmenu) * 1.0) + str(price)
        #Button 클릭 시 호출 함수로 번튼 위치(행, 열) 전달 >> lambda 함수 호출 방식 적용
        Button(w, text=menutxt, command=lambda i=ix, j=iy: btn_menu(i, j), anchor='w', bg="lightgray", fg="navy", relief="raised",
                overrelief="sunken").place(x=xp, y=yp, width=130)
        ix += 1
    iy += 1

ebt = Button(w, text="주문수정", command=set_oqty)
ebt.place(x=30, y=yp+60)

#Text box 생성 (주문내역 표시)
txt1 = Text(w)      #Text 위젯 생성
txt1.place(x=120, y=yp+40, width=550, height=250)

w.mainloop()  # 이벤트 처리를 위해 대기
#################################################