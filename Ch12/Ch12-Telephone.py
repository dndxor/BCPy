import Telzone as tz

def make_menu(menuno):
    print("\n>>번호로 선택: ", end='')
    for no, name in menuno:
        print("[%d] %s " % (no, name), end='   ')
    selnum = int(input("\nNo?> "))
    if selnum >= len(menuno) or selnum < 0:
        print(">>선택 범위 초과!!")
        return -1
    else:
        return selnum

def find_no():  # 지역번호로 검색
    inno = input(">>전화 지역번호 입력: ")
    zone = tz.get_zone(inno)
    print(inno, zone)

def find_zone():  # 지역번호로 검색
    inzone = input(">>전화번호 지역명 입력: ")
    no = tz.get_no(inzone)
    print(inzone, no)

def fpass():  # 없는 메뉴 pass 처리
    pass

menuno = ([0, '종료'], [1, '번호로 검색'], [2, '지역명으로 검색'])  # 메뉴를 위한 튜플 데이터
MENUE_fn = [fpass, find_no, find_zone]  # 호출될 함수명

while True:
    selnum = make_menu(menuno)
    if selnum < 0:
        continue
    if selnum == 0:
        break
    else:
        MENUE_fn[selnum]()  # 리스트 항목에 근거한 함수 호출