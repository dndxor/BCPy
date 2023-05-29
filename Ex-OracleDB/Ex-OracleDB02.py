##[Oracle DB 연동] 테이블 검색 EMP  >  Ex-OracleDB02.py
import cx_Oracle

con = cx_Oracle.connect("scott", "tiger", "192.168.142.72:1521/xe")


# con = cx_Oracle.connect("scott", "tiger", "192.168.142.72:1521/xe", encoding="UTF-8")  #실습 수업용 DB Server

def sel_query(con, sql="Select * from tab"):
    cur = con.cursor()
    cur.execute(sql)
    rows = []  # 검색 결과 행 반환용 리스트
    seq = 0
    for row in cur:
        rows.append(row)
        seq += 1
    print(">>Queried by row count:%2d" % seq)

    return rows


def prt_dept():
    sql = "Select * from dept"  # DEPT 테이블 검색
    rows = sel_query(con, sql)
    for row in rows:
        deptno, dname, loc = row
        print("%5s %25s %15s" % (deptno, dname, loc))


def prt_emp():
    sql = "select empno, ename, job, mgr, to_char(hiredate, 'YYYY/MM/DD'), sal, NVL(comm, 0), deptno from EMP"  # DEPT 테이블 검색
    rows = sel_query(con, sql)
    for row in rows:
        empno, ename, job, mgr, hiredate, sal, comm, deptno = row
        print("%10s %15s %10s %10s %10s" % (empno, ename, job, mgr, hiredate), end='')
        print("%10.1f %10d %5s" % (sal, comm, deptno))


# sql="Select * from tab"  #테이블 검색
# sql = "select column_name, data_type from USER_TAB_COLUMNS where table_name = 'EMP'"  #테이블의 컬럼 검색
prt_dept()  # 부서 테이블 dept 검색
prt_emp()  # 사원 테이블 emp 검색

con.close()