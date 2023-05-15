import os

#소분류 메뉴
menu = {'COFFEE': [['에스프레소', 3.0], ['아메리카노', 3.0], ['카페라떼', 4.0], ['카프치노', 4.0]],
          'LATTE': [['말차라떼', 4.0], ['초코라떼', 4.0], ['카페라떼', 4.0]],
          'TEA': [['청귤차', 4.0], ['자몽차', 4.0], ['레몬차', 4.0], ['카모마일', 4.5]],
          'ADE': [['자몽에이드', 4.5], ['레몬에이드', 4.5], ['청포도에이드', 4.5]],
          'JUICE': [['망고', 4.5], ['바나나', 4.5], ['딸기', 4.5], ['키위', 4.5]],
          'SMOOTHIE': [['청귤스무디', 4.5], ['요거트스무디', 4.5]],
          'MILK TEA': [['흑당밀크티', 4.5], ['달고나밀크티', 4.5]]}

def write_menu_file(menu):
    fpath = os.getcwd()
    fname = fpath + '\\' + "Menu.txt"
    fd = open(fname, 'w')
    for title, mlists in menu.items():
        for mmenu, price in mlists:
            rec = title + '\t' + mmenu + '\t' + str(price) + '\n'
            fd.writelines(rec)
    fd.close()

def read_menu_file():
    global Menu
    fpath = os.getcwd()
    fname = fpath + '\\' + "Menu.txt"
    fd = open(fname, 'r')
    mlist = []
    line = fd.readline()    #한 줄만 읽기
    rec = line.split()
    title, *etc = rec
    save_title = title
    fd.seek(0)
    lcnt = 0
    for line in fd.readlines(): #한 줄씩 반복 읽기
        lcnt += 1
        line = line.rstrip('\n')
        rec = line.split('\t')
        title, mmenu, price = rec
        if save_title != title:
            menu[save_title] = mlist #메뉴 딕셔너리에 추가
            save_title = title
            mlist = []
        mlist.append([mmenu, float(price)])
    if lcnt > 0:
        menu[save_title] = mlist  # 마지막 항목 메뉴 딕셔너리에 추가

def prt_menu(menu):    #(출력)전체(소분류) 메뉴
    print("[[ 메뉴 ]]")
    for title, mlists in menu.items():
        print("## %s ##" %title)
        for menu, price in mlists:
            print("%-10s\t%5.1f" %(menu, price))
        print("")

########## Main ######
write_menu_file(menu)   #딕셔너리를 파일로 쓰기
menu = {}               #기존  딕셔너리 삭제
read_menu_file()        #파일 메뉴를 읽어 딕셔너리로 만들기
print(menu)             #새로운 메뉴 딕셔너리 확인
prt_menu(menu)          #새로운 메뉴 딕셔너리 출력
######################