##[Oracle DB 연동] 테이블 행 추가 : Update Project 테이블  >  Ex-OracleDB06.py
import cx_Oracle

con = cx_Oracle.connect("scott", "tiger", "192.168.142.72:1521/xe")

def sel_query(con, sql=None):
    cur = con.cursor()
    cur.execute(sql)
    rows = []  # 검색 결과 행 반환용 리스트
    seq = 0
    for row in cur:
        rows.append(row)
        seq += 1
    print(">>Queried by row count:%2d" % seq)

    return rows


def in_query(con, sql=None, indata=None):
    cur = con.cursor()
    cur.execute(sql, indata)
    con.commit()


def up_query(con, sql=None, indata=None):
    cur = con.cursor()
    cur.execute(sql, indata)
    con.commit()


def prt_dept():
    sql = "Select * from dept"  # DEPT 테이블 검색
    rows = sel_query(con, sql)
    for row in rows:
        deptno, dname, loc = row
        print("%5s %25s %15s" % (deptno, dname, loc))


def prt_emp():
    sql = "select empno, ename, job, mgr, to_char(hiredate, 'YYYY/MM/DD'), sal, NVL(comm, 0), deptno from EMP"
    rows = sel_query(con, sql)
    for row in rows:
        empno, ename, job, mgr, hiredate, sal, comm, deptno = row
        print("%10s %15s %10s %10s %10s" % (empno, ename, job, mgr, hiredate), end='')
        print("%10.1f %10d %5s" % (sal, comm, deptno))


def prt_empdept():
    sql = "select empno, ename, job, dname from EMP e, DEPT d where e.deptno = d.deptno"
    rows = sel_query(con, sql)
    for row in rows:
        empno, ename, job, dname = row
        print("%10s %15s %10s %15s" % (empno, ename, job, dname))


def prt_empemp():
    sql = "select e1.empno, e1.ename, e1.job, e2.ename, e2.job from EMP e1, EMP e2 where e1.mgr = e2.empno"
    rows = sel_query(con, sql)
    for row in rows:
        empno, ename, ejob, mname, mjob = row
        print("%10s %15s %10s %15s %15s" % (empno, ename, ejob, mname, mjob))


def prt_project():
    sql = "Select * from project"  # DEPT 테이블 검색
    rows = sel_query(con, sql)
    for row in rows:
        pid, pname, pdeptno, pdate = row
        print("%15s %50s %25s %10s" % (pid, pname, pdeptno, pdate))


def insert_project():
    sql = "insert into PROJECT(pid, pname, pdeptno, pdate) " \
          " values (:0, :1, :2, :3)"
    indata = []
    print(">> Project 컬럼 값 입력<<")
    indata.append(input("Project ID >"))
    indata.append(input("Project Name >"))
    indata.append(int(input("Management Deptno >")))
    indata.append(input("Start Date(yyyy/mm/dd) >"))
    print(indata)

    in_query(con, sql, indata)


def update_project():
    pid = input(">> 수정할 Project ID 입력(없으면 Enter) >")
    if len(pid) == 0:
        return
    else:
        sql = f"Select * from project where pid = '{pid}'"
        rows = sel_query(con, sql)
        for row in rows:
            pid, pname, pdeptno, pdate = row
        print(">> 수정할 컬럼 값 입력(없으면 Enter)<<")
        indata = input(f"{pname} >")
        if len(indata) != 0:
            pname = indata
        indata = input(f"{pdeptno} >")
        if len(indata) != 0:
            pdeptno = int(indata)
        indata = input(f"{pdate} >")
        if len(indata) != 0:
            pdeptno = indata
        sql = f"update PROJECT set pname='{pname}', pdeptno={pdeptno}, pdate='{pdate}' " \
              f" where pid = '{pid}'"
        print(sql)
        up_query(con, sql, indata)


# sql="Select * from tab"  #테이블 검색
# sql = "select column_name, data_type from USER_TAB_COLUMNS where table_name = 'EMP'"  #테이블의 컬럼 검색
prt_dept()  # 부서 테이블 dept 검색
prt_emp()  # 사원 테이블 emp 검색
prt_empdept()  # EMP와 DEPT 테이블을 Join 하여 검색
prt_empemp()  # EMP와 EMP 테이블을 Join 하여 검색
# insert_project()  #PROJECT 테이블에 행 추가
prt_project()  # project 테이블 검색
update_project()  # Project 테이블 행 수정

con.close()