## [과제-1/n] Menu.txt 파일을 읽어서 menu 딕셔너리로 만들기 (1) >> read_menu_file()
import os
menu = {}  #파일로부터 만들 메뉴

def read_menu_file():        #파일 메뉴를 읽어 딕셔너리로 만들기
    fpath = os.getcwd()
    fname = fpath + '\\' + "Menu.txt"
    fd = open(fname, 'r')
    mlist = []
    line = fd.readline()    #한 줄만 읽기
    rec = line.split()	  #리스트화
    title, *etc = rec	  #언팩킹
    save_title = title   #변화 탐지용
    fd.seek(0)           #원위치로
    lcnt = 0
    for line in fd.readlines():     #한 줄씩 반복 읽기
        lcnt += 1
        line = line.rstrip('\n')
        rec = line.split('\t')
        title, mmenu, price = rec
        if save_title != title:#title 변화 감지
            menu[save_title] = mlist    #메뉴 딕셔너리에 추가
            save_title = title	#다음 대분류 메뉴 작업 준비
            mlist = []
        mlist.append([mmenu, float(price)])	#소분류 메뉴 리스트 구성
    if lcnt > 0:	#리스트(메뉴)가 존재할 경우
        menu[save_title] = mlist     # 마지막 항목 메뉴 딕셔너리에 추가

def prt_menu(menu):         #새로운 메뉴 딕셔너리 출력
    pass

########## Main ######
read_menu_file()          #파일 메뉴를 읽어 딕셔너리로 만들기
print(menu)               #새로운 메뉴 딕셔너리 확인
prt_menu(menu)         #새로운 메뉴 딕셔너리 출력
######################