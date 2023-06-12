from tkinter import *
import tkinter.messagebox as msgbox
import os
import datetime as dt
from tkcalendar import DateEntry    #tkcalendar 모듈은 명령창에서  pip3 install tkcalendar 실행으로 설치
import matplotlib.pyplot as plt     #matplotlib 모듈은 명령창에서  pip install matplotlib 실행으로 설치

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

def get_order_file():   #주문내역 파일명 얻기(환경 파일로부터)
    try:
        envfname = "EnvFile_Order.txt"
        fd = open(envfname, 'r', encoding='UTF-8')
    except OSError as e:
        print("Error: %s" %e)
    else:
        for line in fd.readlines():
            rec = line.split()  #리스트화
            fname, fdate, dseq = rec   #리스트 슬라이싱
        fd.close()
        return fname

def get_order_dseq():   #주문 일자 순서번호 얻기(환경 파일로부터)
    try:
        envfname = "EnvFile_Order.txt"
        fd = open(envfname, 'r', encoding='UTF-8')
    except OSError as e:
        print("Error: %s" %e)
    else:
        now = dt.datetime.today()
        cdate = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)
        for line in fd.readlines():
            rec = line.split()  #리스트화
            fname, fdate, fdseq = rec   #리스트 슬라이싱
        fd.close()
        if cdate != fdate:
            return 0    #신규 일자는 0으로 시작
        else:
            return fdseq #기존 일자는 저장값 반환

def set_order_dseq(dseq):   #주문 일자 순서번호 갱신하기(환경 파일에)
    try:
        envfname = "EnvFile_Order.txt"
        fd = open(envfname, 'r+', encoding='UTF-8')
    except OSError as e:
        print("Error: %s" %e)
    else:
        for line in fd.readlines():
            rec = line.split()  #리스트화
            fname, fdate, fdseq = rec   #리스트 슬라이싱
        now = dt.datetime.today()
        cdate = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)
        line = fname + '\t' + cdate + '\t' + str(dseq)
        fd.seek(0)  #처음으로 가서 덮어쓰기
        fd.writelines(line)
        fd.close()

def append_order_file(orders):   #주문내역 리스트를 파일로 저장
    ofname = get_order_file()       #주문내역 파일명 얻기
    fd = open(ofname, 'a')
    dseq = int(get_order_dseq())    #일일 중 일련번호 얻기
    oseq = 0    #주문 중 일련번호
    dseq += 1
    now = dt.datetime.today()
    cdate = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)
    orderid =  cdate + str(dseq).zfill(5)
    for mmenu, olist in orders.items():
        munit, mqty, mtot = olist
        oseq += 1
        rec = orderid+'\t'+str(oseq).zfill(2)
        rec += '\t' + mmenu + '\t' + str(munit) + '\t' + str(mqty) + '\t' + str(mtot) +'\n'
        fd.writelines(rec)
    fd.close()
    return dseq

def order_ok():
    if len(orders) <= 0:
        msgbox.showinfo("선택 메뉴 없음", "메뉴 버튼을 눌러 주문을 먼저 하세요.")
        return
    dseq = append_order_file(orders)  # 주문내역 파일로 저장
    set_order_dseq(dseq)  # 일일 주문 일련번호 갱신
    msgbox.showinfo("주문 완료", "주문이 정상처리 되었습니다.(수정 불가)")
    new_order()

def new_order():
    orders.clear()
    txt1.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)

def win_close(win):
#    win.quit()
    win.destroy()

def TLW_all_menu():     #소분류 메뉴 보기(TopLevel 창으로)
    global menu
    tlw_11 = Toplevel(w)
    tlw_11.title("전체_메뉴 구성")
    tlw_11.geometry("400x450+600+40")
    tlw_11.resizable(1, 1)

    txt_11 = Text(tlw_11)  # Text 위젯 생성
    txt_11.place(x=4, y=4, width=400, height=400)
    #    txt.grid(row=0,column=0)
    Button(tlw_11, text="닫기", command=lambda win=tlw_11: win_close(win)).place(x=200, y=420)

    txt_11.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
    for title, mlists in menu.items():
        seq = 0
        for menu, price in mlists:
            seq += 1
            line = "## {0:^10} ## [{1:1}] {2:<12} {3:>4}".format(title, seq, menu, price)
            txt_11.insert(CURRENT, line+'\n')
        line = "-"*50
        txt_11.insert(CURRENT, line+'\n')

def TLW_top_menu():     #대분류 메뉴 보기(TopLevel 창으로)
    global menugroup
    tlw_12 = Toplevel(w)
    tlw_12.title("대분류 매뉴 구성")
    tlw_12.geometry("400x450+600+40")
    tlw_12.resizable(1, 1)

    txt_12 = Text(tlw_12)  # Text 위젯 생성
    txt_12.place(x=4, y=4, width=400, height=400)
    #    txt.grid(row=0,column=0)
    Button(tlw_12, text="닫기", command=lambda win=tlw_12: win_close(win)).place(x=200, y=420)

    txt_12.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
    for no, title in menugroup.items():
        line = "[{0:1}] {1:<12}".format(no, title)
        txt_12.insert(CURRENT, line+'\n')

def TLW_order_list():       #현재 진행중인 주문내역 orders 딕셔너리 내용 보기 (TopLevel 창으로)
    global orders
    tlw_21 = Toplevel(w)
    tlw_21.title("주문내역 (전체)")
    tlw_21.geometry("500x360+600+40")
    tlw_21.resizable(1, 1)

    txt_21 = Text(tlw_21)  # Text 위젯 생성
    txt_21.place(x=4, y=4, width=460, height=300)
    #    txt.grid(row=0,column=0)
    Button(tlw_21, text="닫 기", command=lambda win=tlw_21: win_close(win)).place(x=220, y=320)
    txt_21.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)

    line = "{0:^3} {1:^8} {2:^8} {3:^8} {4:^8}".format("순번", "주문_메뉴", "단가(천원)", "주문_수량", "주문금액(원)")
    txt_21.insert(CURRENT, line + '\n')
    line = '-' * 60
    txt_21.insert(CURRENT, line + '\n')

    totorder, totqty, seq = (0, 0, 0)
    for mmenu, olist in orders.items():
        munit, mqty, mtot = olist
        totorder += mtot
        totqty += mqty
        seq += 1   	#순서번호 생성
        line = "[{0:>2}] {1:<12} {2:>4} {3:>10} {4:>16}".format(seq, mmenu, munit, mqty, mtot)
        txt_21.insert(CURRENT, line+'\n')
    line = "-"*60
    txt_21.insert(CURRENT, line+'\n')
    line = "*메뉴 수:{0:>2}    *수량 계: {1:>2}   *합계 금액: {2:>10}".format(seq, totqty, totorder)
    txt_21.insert(CURRENT, line+'\n')
    line = "-"*60
    txt_21.insert(CURRENT, line+'\n')

def TLW_orders_all_list():       #주문내역 Orders_2022.txt 파일 내용 보기 (TopLevel 창으로)
    tlw_22 = Toplevel(w)
    tlw_22.title("주문내역 (전체)")
    tlw_22.geometry("540x380+600+40")
    tlw_22.resizable(1, 1)

    txt_22 = Text(tlw_22)  # Text 위젯 생성
    txt_22.place(x=4, y=4, width=530, height=340)
    #    txt.grid(row=0,column=0)
    Button(tlw_22, text="닫 기", command=lambda win=tlw_22: win_close(win)).place(x=220, y=350)
    txt_22.delete(1.0, 100.100)   #이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)

    line = "{0:^3} {1:^10} {2:^11} {3:^8} {4:^8} {5:^8}".format("순번", "주문번호", "주문_메뉴", "단가(천원)", "주문_수량", "주문금액(원)")
    txt_22.insert(CURRENT, line + '\n')
    line = '-'*75
    txt_22.insert(CURRENT, line + '\n')

    try:
        ofname = get_order_file()   #주문내역 파일명 얻기
        fd = open(ofname, 'r')
    except OSError as e:
        print("Error: %s" %e)
    else:
        seq = 0
        for line in fd.readlines():
            rec = line.split()  #리스트화
            oid, dseq, mmenu, munit, mqty, mtot = rec   #리스트 슬라이싱
            seq += 1
            line = "[{0:>3}] {1:13}-{2:<2} {3:<12} {4:>4} {5:>10} {6:>16}".format(seq, oid, dseq, mmenu, munit, mqty, mtot)
            txt_22.insert(CURRENT, line+'\n')

def TLW_orders_term_list():       #주문내역 Orders_2022.txt 파일 내용 <전체> 보기 (TopLevel 창으로)
    ##주문내역 파일 읽어오기
    def find_order_file():
        txt_23.delete(1.0, 100.100)  # 이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
        fromDate = cal_f.get().replace('/','')
        toDate = cal_t.get().replace('/','')

        line = "{0:^3} {1:^10} {2:^11} {3:^8} {4:^8} {5:^8}".format("순번", "주문번호", "주문_메뉴", "단가(천원)", "주문_수량", "주문금액(원)")
        txt_23.insert(CURRENT, line + '\n')
        line = '-'*75
        txt_23.insert(CURRENT, line + '\n')

        try:
            ofname = get_order_file()  # 주문내역 파일명 얻기
            fd = open(ofname, 'r')
        except OSError as e:
            print("Error: %s" % e)
        else:
            seq = 0
            for line in fd.readlines():
                rec = line.split()  # 리스트화
                oid, dseq, mmenu, munit, mqty, mtot = rec  # 리스트 슬라이싱
                if str(oid[:8]) < fromDate or str(oid[:8]) > toDate:
                    continue
                seq += 1
                line = "[{0:>3}] {1:13}-{2:<2} {3:<12} {4:>4} {5:>10} {6:>16}".format(seq, oid, dseq, mmenu, munit,
                                                                                      mqty,
                                                                                      mtot)
                txt_23.insert(CURRENT, line + '\n')
    ##화면 구성
    tlw_23 = Toplevel(w)
    tlw_23.title("(완결된)주문내역 <기간으로>보기")
    tlw_23.geometry("580x460+600+40")
    tlw_23.resizable(1, 1)

    Label(tlw_23, text='').grid(row=0, columnspan=6)
    Label(tlw_23,text='시작 일자').grid(row=1, column=0)
    cal_f = DateEntry(tlw_23, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_f.grid(row=1, column=1, sticky='nsew')
    Label(tlw_23,text='종료 일자').grid(row=1, column=2)
    cal_t = DateEntry(tlw_23, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_t.grid(row=1, column=3, sticky='nsew')
    Button(tlw_23, text="검 색", command=find_order_file).grid(row=1, column=5)
    Label(tlw_23, text='').grid(row=2, columnspan=6)
    txt_23 = Text(tlw_23)  # Text 위젯 생성
    txt_23.grid(row=3, columnspan=6)
    Label(tlw_23, text='').grid(row=4, columnspan=6)
    Button(tlw_23, text="닫 기", command=lambda win=tlw_23: win_close(win)).grid(row=5, columnspan=6)

def TLW_daily_stats():       #<일자별>로 요약된 매출 정보 (TopLevel 창으로)
    ##주문내역 파일 읽어오기
    def stats_order_daily():
        txt_31.delete(1.0, 100.100)  # 이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
        fromDate = cal_f.get().replace('/','')
        toDate = cal_t.get().replace('/','')
        try:
            ofname = get_order_file()  # 주문내역 파일명 얻기
            fd = open(ofname, 'r')
        except OSError as e:
            print("Error: %s" % e)
        else:
            line = "{0:^3} {1:^10} {2:^13} {3:^7} {4:^10} {5:^10}".format("순번", "일자", "주문_수", "메뉴_수", "수량", "총_매출(원)")
            txt_31.insert(CURRENT, line + '\n')
            line = '-'*80
            txt_31.insert(CURRENT, line + '\n')
            rcnt = 0
            seq = 0
            cnt_order, cnt_menu, cnt_qty, tot_won = (0, 0, 0, 0)
            for line in fd.readlines():
                rec = line.split()  # 리스트화
                oid, dseq, mmenu, munit, mqty, mtot = rec  # 리스트 슬라이싱
                cur_day = str(oid[:8])
                if cur_day < fromDate or cur_day > toDate:
                    continue
                if rcnt == 0:
                    new_day = cur_day
                    new_oid = oid
                rcnt += 1
                if new_oid != oid:
                    cnt_order += 1
                    new_oid = oid
                if new_day == cur_day:
                    cnt_menu += 1
                    cnt_qty += int(mqty)
                    tot_won += int(mtot.replace('.', ''))/10
                else:
                    seq += 1
                    oday = new_day[:4]+'/'+new_day[4:6]+'/'+new_day[6:]
                    line = "[{0:>2}] {1:<10} {2:>12} {3:>12} {4:>12} {5:>16}".format(seq, oday, cnt_order, cnt_menu, cnt_qty, tot_won)
                    txt_31.insert(CURRENT, line + '\n')
                    new_day = cur_day
                    cnt_order, cnt_menu = (0, 1)
                    cnt_qty, tot_won = (int(mqty), int(mtot.replace('.', ''))/10)
            if rcnt > 0:
                seq += 1
                cnt_order += 1
                oday = new_day[:4] + '/' + new_day[4:6] + '/' + new_day[6:]
                line = "[{0:>2}] {1:<10} {2:>12} {3:>12} {4:>12} {5:>16}".format(seq, oday, cnt_order, cnt_menu, cnt_qty, tot_won)
                txt_31.insert(CURRENT, line + '\n')
    ##화면 구성
    tlw_31 = Toplevel(w)
    tlw_31.title("일자별 매출 내역 <통계>")
    tlw_31.geometry("600x460+600+40")
    tlw_31.resizable(1, 1)

    Label(tlw_31, text='').grid(row=0, columnspan=6)
    Label(tlw_31,text='시작 일자').grid(row=1, column=0)
    cal_f = DateEntry(tlw_31, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_f.grid(row=1, column=1, sticky='nsew')
    Label(tlw_31,text='종료 일자').grid(row=1, column=2)
    cal_t = DateEntry(tlw_31, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_t.grid(row=1, column=3, sticky='nsew')
    Button(tlw_31, text="통계 보기", command=stats_order_daily).grid(row=1, column=5)
    Label(tlw_31, text='').grid(row=2, columnspan=6)
    txt_31 = Text(tlw_31)  # Text 위젯 생성
    txt_31.grid(row=3, columnspan=6)
    Label(tlw_31, text='').grid(row=4, columnspan=6)
    Button(tlw_31, text="닫 기", command=lambda win=tlw_31: win_close(win)).grid(row=5, columnspan=6)

def TLW_monthly_stats():       #<월별>로 요약된 매출 정보 (TopLevel 창으로)
    ##주문내역 파일 읽어오기
    def stats_order_monthly():
        txt_32.delete(1.0, 100.100)  # 이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
        fromDate = cal_f.get().replace('/','')
        toDate = cal_t.get().replace('/','')
        fromMonth = fromDate[:-2]
        toMonth = toDate[:-2]
        print(fromMonth, toMonth)
        try:
            ofname = get_order_file()  # 주문내역 파일명 얻기
            fd = open(ofname, 'r')
        except OSError as e:
            print("Error: %s" % e)
        else:
            line = "{0:^3} {1:^10} {2:^13} {3:^7} {4:^10} {5:^10}".format("순번", "월", "주문_수", "메뉴_수", "수량", "총_매출(원)")
            txt_32.insert(CURRENT, line + '\n')
            line = '-'*80
            txt_32.insert(CURRENT, line + '\n')
            rcnt = 0
            seq = 0
            cnt_order, cnt_menu, cnt_qty, tot_won = (0, 0, 0, 0)
            for line in fd.readlines():
                rec = line.split()  # 리스트화
                oid, dseq, mmenu, munit, mqty, mtot = rec  # 리스트 슬라이싱
                cur_day = str(oid[:8])
                cur_month = str(oid[:6])
                if cur_day < fromDate or cur_day > toDate:
                    continue
                if rcnt == 0:
                    new_month = cur_month
                    new_oid = oid
                rcnt += 1
                if new_oid != oid:
                    cnt_order += 1
                    new_oid = oid
                if new_month == cur_month:
                    cnt_menu += 1
                    cnt_qty += int(mqty)
                    tot_won += int(mtot.replace('.', ''))/10
                else:
                    seq += 1
                    omonth = new_month[:4]+'/'+new_month[4:6]
                    line = "[{0:>2}] {1:<10} {2:>12} {3:>12} {4:>12} {5:>16}".format(seq, omonth, cnt_order, cnt_menu, cnt_qty, tot_won)
                    txt_32.insert(CURRENT, line + '\n')
                    new_month = cur_month
                    cnt_order, cnt_menu = (0, 1)
                    cnt_qty, tot_won = (int(mqty), int(mtot.replace('.', ''))/10)
            if rcnt > 0:
                seq += 1
                cnt_order += 1
                omonth = new_month[:4] + '/' + new_month[4:6]
                line = "[{0:>2}] {1:<10} {2:>12} {3:>12} {4:>12} {5:>16}".format(seq, omonth, cnt_order, cnt_menu, cnt_qty, tot_won)
                txt_32.insert(CURRENT, line + '\n')
    ##화면 구성
    tlw_32 = Toplevel(w)
    tlw_32.title("월별 매출 내역 <통계>")
    tlw_32.geometry("600x460+600+40")
    tlw_32.resizable(1, 1)

    Label(tlw_32, text='').grid(row=0, columnspan=6)
    Label(tlw_32,text='시작 일자').grid(row=1, column=0)
    cal_f = DateEntry(tlw_32, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_f.grid(row=1, column=1, sticky='nsew')
    Label(tlw_32,text='종료 일자').grid(row=1, column=2)
    cal_t = DateEntry(tlw_32, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_t.grid(row=1, column=3, sticky='nsew')
    Button(tlw_32, text="통계 보기", command=stats_order_monthly).grid(row=1, column=5)
    Label(tlw_32, text='').grid(row=2, columnspan=6)
    txt_32 = Text(tlw_32)  # Text 위젯 생성
    txt_32.grid(row=3, columnspan=6)
    Label(tlw_32, text='').grid(row=4, columnspan=6)
    Button(tlw_32, text="닫 기", command=lambda win=tlw_32: win_close(win)).grid(row=5, columnspan=6)

def TLW_daily_fig(figno):       #<일자별>로 요약된 매출 차트 (TopLevel 창으로))
    ##주문내역 파일 읽어오기
    def chart_order_daily():
        txt_41.delete(1.0, 100.100)  # 이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
        fromDate = cal_f.get().replace('/','')
        toDate = cal_t.get().replace('/','')
        olist_day = []
        olist_order = []
        olist_dqty = []
        olist_dwon = []

        try:
            ofname = get_order_file()  # 주문내역 파일명 얻기
            fd = open(ofname, 'r')
        except OSError as e:
            print("Error: %s" % e)
        else:
            rcnt = 0
            seq = 0
            cnt_order, cnt_menu, cnt_qty, tot_won = (0, 0, 0, 0)
            for line in fd.readlines():
                rec = line.split()  # 리스트화
                oid, dseq, mmenu, munit, mqty, mtot = rec  # 리스트 슬라이싱
                cur_day = str(oid[:8])
                if cur_day < fromDate or cur_day > toDate:
                    continue
                if rcnt == 0:
                    new_day = cur_day
                    new_oid = oid
                rcnt += 1
                if new_oid != oid:
                    cnt_order += 1
                    new_oid = oid
                if new_day == cur_day:
                    cnt_menu += 1
                    cnt_qty += int(mqty)
                    tot_won += int(mtot.replace('.', ''))/10
                else:
                    seq += 1
                    oday = new_day[:4]+'/'+new_day[4:6]+'/'+new_day[6:]
                    olist_day.append(oday)
                    olist_order.append(cnt_order)
                    olist_dqty.append(cnt_qty)
                    olist_dwon.append(tot_won)
                    new_day = cur_day
                    cnt_menu = 1
                    cnt_qty, tot_won = (int(mqty), int(mtot.replace('.', ''))/10)
            if rcnt > 0:
                oday = new_day[:4] + '/' + new_day[4:6] + '/' + new_day[6:]
                olist_day.append(oday)
                olist_order.append(cnt_order)
                olist_dqty.append(cnt_qty)
                olist_dwon.append(tot_won)

            def txt_list(figno):  # TextBox에 통계 값 출력
                if figno == 1:
                    line = "순위  판매_일자        매출_금액(원)"
                elif figno == 2:
                    line = "순위  판매_일자        주문_횟수   주문_수량"
                txt_41.insert(CURRENT, line + '\n')
                for i in range(len(olist_day)):     #일자 기준 출력 통제
                    if figno == 1:      #금액 기준 출력
                        line = "[{0:>2}] {1:^12} {2:>15}".format(i+1, olist_day[i], olist_dwon[i])
                    elif figno == 2:    #주문 횟수와 수량 기준 출력
                        line = "[{0:>2}] {1:^12} {2:>10} {3:>12}".format(i+1, olist_day[i], olist_order[i], olist_dqty[i])
                    txt_41.insert(CURRENT, line + '\n')

            txt_list(figno)  # 통계값 TextBox에 출력

            ##x-y 차트로 확인하기
            plt.rcParams['font.family'] = 'Malgun Gothic'   #한글 폰트 해결
            plt.rcParams['axes.unicode_minus'] = False     #한글 폰트 해결
            if figno == 1:
                plt.title("메뉴별 총 매출금액 비교 차트")
                plt.xlabel("메뉴명")
                plt.ylabel("총 매출금액(원)")
                plt.bar(olist_day, olist_dwon)
                for i in range(len(olist_dwon)):     #그래프에 y-축 값 표시
                    plt.text(olist_day[i], olist_dwon[i], olist_dwon[i])
            elif figno == 2:
                plt.title("메뉴별 주문 건수/수량 비교 차트")
                plt.xlabel("일자")
                plt.ylabel("주문 횟수/수량")
                plt.plot(olist_day, olist_order, label='주문_횟수', ls='--', marker='*')
                plt.plot(olist_day, olist_dqty, label='주문_수량', ls=':', marker='p')
                for i in range(len(olist_order)):     #그래프에 y-축 값 표시
                    plt.text(olist_day[i], olist_order[i], olist_order[i])
                for i in range(len(olist_dqty)):     #그래프에 y-축 값 표시
                    plt.text(olist_day[i], olist_dqty[i], olist_dqty[i])
                plt.legend()
            plt.show()

    ##화면 구성
    tlw_41 = Toplevel(w)
    tlw_41.title("일자별 매출내역 비교 <차트>")
    tlw_41.geometry("600x460+600+40")
    tlw_41.resizable(1, 1)

    Label(tlw_41, text='').grid(row=0, columnspan=6)
    Label(tlw_41,text='시작 일자').grid(row=1, column=0)
    cal_f = DateEntry(tlw_41, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_f.grid(row=1, column=1, sticky='nsew')
    Label(tlw_41,text='종료 일자').grid(row=1, column=2)
    cal_t = DateEntry(tlw_41, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_t.grid(row=1, column=3, sticky='nsew')
    Button(tlw_41, text="차트 보기", command=chart_order_daily).grid(row=1, column=5)
    Label(tlw_41, text='').grid(row=2, columnspan=6)
    txt_41 = Text(tlw_41)  # Text 위젯 생성,
    txt_41.grid(row=3, columnspan=6)
    Label(tlw_41, text='').grid(row=4, columnspan=6)
    Button(tlw_41, text="닫 기", command=lambda win=tlw_41: win_close(win)).grid(row=5, columnspan=6)

def TLW_menu_fig(figno):       #<메뉴별>로 상위 5개 매출 / 수량 비교 차트 (TopLevel 창으로))
    ##주문내역 파일 읽어오기
    def chart_order_menu():
        txt_43.delete(1.0, 100.100)  # 이전 내용 삭제 (1번째 줄 0번째 문자부터 100번째 줄 100번째 문자까지)
        fromDate = cal_f.get().replace('/','')
        toDate = cal_t.get().replace('/','')
        olist_sel = []
        olist_wmenu, olist_qmenu = ([], [])
        olist_qty, olist_mqty = ([], [])
        olist_won, olist_mwon = ([], [])
        ##Orders.txt 파일을 읽어서 olist_menu 리스트 생성
        try:
            ofname = get_order_file()  # 주문내역 파일명 얻기
            fd = open(ofname, 'r')
        except OSError as e:
            print("Error: %s" % e)
        else:
            for line in fd.readlines():
                rec = line.split()  # 리스트화
                oid, dseq, mmenu, munit, mqty, mtot = rec  # 리스트 슬라이싱
                cur_day = str(oid[:8])
                if cur_day < fromDate or cur_day > toDate:
                    continue
                olist_sel.append([mmenu, rec])

        olist_sel = sorted(olist_sel)   #메뉴명으로 sorting
        rcnt = 0
        cnt_order, cnt_menu, cnt_qty, tot_won = (0, 0, 0, 0)
        total_won = 0   #선택 기간 내의 총 매출 금액 구하기
        for mmenu, olist in olist_sel:
            oid, dseq, mmenu, munit, mqty, mtot = olist  # 리스트 슬라이싱
            total_won += int(mtot.replace('.', ''))/10
        for mmenu, olist in olist_sel:
            oid, dseq, mmenu, munit, mqty, mtot = olist  # 리스트 슬라이싱
            if rcnt == 0:   #최초에 메뉴명 초기화(메뉴명 변화를 감지하기 위해)
                new_menu = mmenu
            rcnt += 1
            if new_menu != mmenu:      #메뉴가 바뀌면 이전 메뉴의 통계값 각 리스트에 추가
                olist_mqty.append([cnt_qty, new_menu])
                olist_mwon.append([tot_won/total_won*100, new_menu])
                new_menu = mmenu
                cnt_menu = 1
                cnt_qty, tot_won = (int(mqty), int(mtot.replace('.', ''))/10)
            else:   #메뉴별 통계값 누적
                cnt_menu += 1
                cnt_qty += int(mqty)
                tot_won += int(mtot.replace('.', ''))/10
        if rcnt > 0:    #마지막 메뉴 통계값 별도 추가
            olist_mqty.append([cnt_qty, new_menu])
            olist_mwon.append([tot_won/total_won*100, new_menu])

        olist_mqty = sorted(olist_mqty, reverse=True)     #수량 기준으로 sorting
        olist_mwon = sorted(olist_mwon, reverse=True)     #매출 기준으로 sorting
        num_top = 5     #보기를 원하는 top rank 수
        cnt_rank = 0
        for qty, mmenu in olist_mqty:
            if cnt_rank >= num_top:         #매출 수량 상위 num_top만큼 선택
                break
            else:
                cnt_rank += 1
            olist_qty.append(qty)           #sorting된 리스트에서 수량만 리스트로 구성(y-축)
            olist_qmenu.append(mmenu)       #sorting된 리스트에서 메뉴만 리스트로 구성(x-축)
        cnt_rank = 0
        for won, mmenu in olist_mwon:
            if cnt_rank >= num_top:         #매출 금액 상위 num_top만큼 선택
                break
            else:
                cnt_rank += 1
            olist_won.append(won)           #sorting된 리스트에서 매출만 리스트로 구성(x-축)
            olist_wmenu.append(mmenu)       #sorting된 리스트에서 메뉴만 리스트로 구성(x-축)

        def txt_list(figno):    #TextBox에 통계 값 출력
            if figno == 1:
                olist = olist_mwon
                line = "순위   메뉴명              매출 비율(%)"
            elif figno == 2:
                olist = olist_mqty
                line = "순위   메뉴명              판매 수량"
            txt_43.insert(CURRENT, line + '\n')
            seq = 0
            for x, mmenu in olist:  #x는 매출 또는 수량
                seq += 1
                line = "[{0:>2}] {1:<10} {2:>10}".format(seq, mmenu, x)
                txt_43.insert(CURRENT, line + '\n')

        txt_list(figno)     #통계값 TextBox에 출력

        ##x-y 차트로 확인하기
        plt.rcParams['font.family'] = 'Malgun Gothic'   #한글 폰트 해결
        plt.rcParams['axes.unicode_minus'] = False     #한글 폰트 해결
        if figno == 1:
            plt.title("메뉴별 매출금액 비율(%) 비교 차트 (Top 5)")
            plt.pie(olist_won, labels=olist_wmenu, autopct='%.1f%%')
        elif figno == 2:
            plt.title("메뉴별 주문 수량 비교 차트 (Top 5)")
            plt.xlabel("메뉴명")
            plt.ylabel("판매 수량")
            plt.plot(olist_qmenu, olist_qty, label='주문_수량', ls=':', marker='p')
            for i in range(len(olist_qty)):     #그래프에 y-축 값 표시
                plt.text(olist_wmenu[i], olist_qty[i], olist_qty[i])
            plt.legend()
        plt.show()

    ##화면 구성
    tlw_43 = Toplevel(w)
    tlw_43.title("메뉴별 매출 및 주문수량 비교 <차트>")
    tlw_43.geometry("600x460+600+40")
    tlw_43.resizable(1, 1)

    Label(tlw_43, text='').grid(row=0, columnspan=6)
    Label(tlw_43,text='시작 일자').grid(row=1, column=0)
    cal_f = DateEntry(tlw_43, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_f.grid(row=1, column=1, sticky='nsew')
    Label(tlw_43,text='종료 일자').grid(row=1, column=2)
    cal_t = DateEntry(tlw_43, date_pattern='yyyy/mm/dd', width=12, background='darkblue',
                    foreground='white', borderwidth=4, Calendar=2018)
    cal_t.grid(row=1, column=3, sticky='nsew')
    Button(tlw_43, text="차트 보기", command=chart_order_menu).grid(row=1, column=5)
    Label(tlw_43, text='').grid(row=2, columnspan=6)
    txt_43 = Text(tlw_43)  # Text 위젯 생성,
    txt_43.grid(row=3, columnspan=6)
    Label(tlw_43, text='').grid(row=4, columnspan=6)
    Button(tlw_43, text="닫 기", command=lambda win=tlw_43: win_close(win)).grid(row=5, columnspan=6)

############# Main ###############################
new_menugroup()     #menu(소분류) 딕셔너리로부터 menugroup(대분류) 딕셔너리 구성

#기본 윈도우 생성
w = Tk()
w.title("부천대학 컴퓨터소프트웨어과 Dreammer Cafe")      #윈도우 타이틀("제목")
w.geometry("700x500+20+20")     #윈도우 크기 및 기준점("너비x높이+x좌표+y좌표")
w.resizable(1, 1)       #창 크기 조절 가능 여부(상하, 좌우)

##메뉴 생성
menubar=Menu(w)

menu_1=Menu(menubar, tearoff=0)
menu_1.add_command(label="전체_메뉴 보기", command=TLW_all_menu)
menu_1.add_command(label="대분류_메뉴 보기", command=TLW_top_menu)
menu_1.add_separator()
menu_1.add_command(label="종료", command=lambda win=w: win_close(win))
menubar.add_cascade(label="검색", menu=menu_1)
w.config(menu=menubar)

menu_2=Menu(menubar, tearoff=0)
menu_2.add_command(label="(진행중인)주문내역 보기", command=TLW_order_list)
menu_2.add_command(label="(완결된)주문내역 <전체>보기", command=TLW_orders_all_list)
menu_2.add_command(label="(완결된)주문내역 <기간>보기", command=TLW_orders_term_list)
menubar.add_cascade(label="주문내역", menu=menu_2)

menu_3=Menu(menubar, tearoff=0)
menu_3.add_command(label="일자별 매출 내역", command=TLW_daily_stats)
menu_3.add_command(label="월별 매출 내역", command=TLW_monthly_stats)
#menu_3.add_command(label="분기별 매출 내역", command=TLW_quters_stats)
menubar.add_cascade(label="매출_통계", menu=menu_3)

menu_4=Menu(menubar, tearoff=0)
menu_4.add_command(label="일자별 총 매출금액 비교 차트", command=lambda figno=1: TLW_daily_fig(figno))
menu_4.add_command(label="일자별 총 주문 건수/수량 비교 차트", command=lambda figno=2: TLW_daily_fig(figno))
menu_4.add_separator()
menu_4.add_command(label="메뉴별 총 매출금액 비교 차트", command=lambda figno=1: TLW_menu_fig(figno))
menu_4.add_command(label="메뉴별 주문 수량 비교 차트", command=lambda figno=2: TLW_menu_fig(figno))
menubar.add_cascade(label="매출_차트", menu=menu_4)

#menu 딕셔너리 기반 주문 버튼 생성
ix, iy = (0, 0)
xp, yp = (0, 0)
for menugrp, mlist in menu.items():
    xp = 10
    yp = 10 + iy * 30
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

ebt = Button(w, text="주문 수정", command=set_oqty)
ebt.place(x=30, y=yp+60)
nobt = Button(w, text="[취소]재시작", command=new_order)
nobt.place(x=30, y=yp+60+200)

#Text box 생성 (주문내역 표시)
txt1 = Text(w)      #Text 위젯 생성
txt1.place(x=120, y=yp+40, width=550, height=200)

obt = Button(w, text="주문 확정", command=order_ok)
obt.place(x=330, y=yp+60+200)

w.mainloop()  # 이벤트 처리를 위해 대기
#################################################