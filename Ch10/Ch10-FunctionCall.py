### [함수호출 방법] 함수형 변수로 호출  >> Ch10-FunctionCall.py
def find_student():  ##TASKS_fn[1][1] : 학번으로 student 딕셔너리 검색
    pass

def find_dept():  ##TASKS_fn[1][2] : 부서코드로 dept 딕셔너리 검색
    pass

def find_prof():  ##TASKS_fn[1][3] : 교수아이디로 prof 딕셔너리 검색
    pass

def find_subject():  ##TASKS_fn[1][4] : 과목코드로 subject 딕셔너리 검색
    pass

def find_stscore():  ##TASKS_fn[1][5] : 학번으로 stscore 리스트 검색
    pass

def list_stscore_st():  ##TASKS_fn[1][1] : 학번으로 stscore 출력
    pass

def list_stscore_sub():  ##TASKS_fn[1][2] : 과목코드로 stscore 출력
    pass

def in_stscore_list():  ##TASKS_fn[4][5] : stscore 리스트 추가 및 성적.txt 파일 갱신
    pass

def fpass():  # 없는 메뉴 pass 처리
    pass

def sel_tasks(idx):  ##(최상위) 작업 메뉴 선택
    while True:
        tlen = 0
        for x in TASKS[idx]:
            tlen += len(x) * 2 + 5  # 타이틀 문자 수 계산
        print("_" * tlen)
        seq = 0
        print("[%s]" % MENUS.get(idx), end=' ')  # 메뉴 그룹 표시(Top, 검색, 현황, ...)
        for mname in TASKS[idx]:  # 선택 가능 차상위 메뉴 표시
            print("%d:%s" % (seq, mname), end='   ')
            seq += 1
        selno = input("\n[작업 선택]> ")
        if len(selno) == 0:
            selno = '0'
        if int(selno) >= len(TASKS[idx]):  # 선택 범위 초과
            continue
        return int(selno)

def task_fn_call(idx):  ##(차상위) 작업 메뉴 선택 및 관련 함수 호출
    while True:
        selno = sel_tasks(idx)  # 선택된 최상위 메뉴에 대한 차상위 메뉴 선택 호출
        if selno != 0:
            print("[[%s: %s]]" % (MENUS.get(idx), TASKS[idx][selno]))
        if selno == 0:
            break
        else:
            TASKS_fn[idx][selno]()  # 선택 작업 관련 함수 호출

MENUS = {0: 'Top:', 1: '검색', 2: '현황', 3: '통계', 4: '데이터관리'}  # 최상위 메뉴
TASKS = [['종료', '검색', '현황', '통계', '데이터관리'],  # 최상위 메뉴 구성
         ['복귀', '학생', '학과', '교수', '과목', '성적'],  # 차상위 메뉴(검색)
         ['복귀', '성적_통지서', '과목별_성적'],  # 차상위 메뉴(현황)
         ['복귀', '과목_성적', '교수_과목', '학과_과목', '학과_교수'],  # 차상위 메뉴(통계)
         ['복귀', '학생', '학과', '교수', '과목', '성적']]  # 차상위 메뉴(데이터관리)
TASKS_fn = [[fpass, fpass, fpass, fpass, fpass],  # 차상위 메뉴 호출 함수명(TASKS와 대응)
       [fpass, find_student, find_dept, find_prof, find_subject, find_stscore],  # 차상위 메뉴 함수(검색)
       [fpass, list_stscore_st, list_stscore_sub],  # 차상위 메뉴 함수(현황)
       [fpass, fpass, fpass, fpass, fpass],  # 차상위 메뉴 함수(통계)
       [fpass, in_stscore_list, fpass, fpass, fpass, fpass]]  # 차상위 메뉴 함수(데이터관리)

########## Main ###################################
while True:  # 작업 선택
    selno = sel_tasks(0)  # 상위 작업 번호 선택
    if selno == 0:
        break
    else:
        task_fn_call(selno)  # 하위 작업 선택 및 관련 함수 호출
####################################################