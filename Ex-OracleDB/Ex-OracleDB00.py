##[Oracle DB 연동] 테이블 확인
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
    print(">>Queried row count:%2d" % seq)

    return rows


# sql="Select * from tab"  #테이블 검색
sql = "select column_name, data_type, data_length from USER_TAB_COLUMNS where table_name = 'EMP'"  # 테이블의 컬럼 검색
# sql="Select * from dept"  #DEPT 테이블 검색
rows = sel_query(con, sql)
for row in rows:
    print(row)

con.close()