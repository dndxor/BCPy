# 환율 계산기

from tkinter import *

def calc_money(e) :     # 함수 정의
    moneyInfo = {1:(1188.50, "달러"), 2:(1570.13, "파운드"),
                 3:(15.01, "루블"), 4:(173.93, "위안")}
    n = nation.get()    # 국가 번호 추출
    try :
        money = int(en.get()) # 금액 추출(문자열), 정수형으로 변환
    except :
        result.config(text="금액은 정수형으로 입력하세요.")
    else :
        rate, unit = moneyInfo.get(n)   # 검색한 결과를 두 변수에 담기
        result.config(text="%.2f %s" % (money/rate, unit)) # 레이블에 결과 표시
      
w = Tk()
w.title("환율 계산기")

# 국가 선택
Label(w, text="환전하려는 국가를 선택하세요.", bg="lightgray", width=40).pack()
nation = IntVar() # 선택한 국가를 저장하는 변수
nation.set(1)# 기본 값을 "미국"으로 설정
rb1 = Radiobutton(w, text="미국", variable=nation, value=1).pack()
rb2 = Radiobutton(w, text="영국", variable=nation, value=2).pack()
rb3 = Radiobutton(w, text="러시아", variable=nation, value=3).pack()
rb4 = Radiobutton(w, text="중국", variable=nation, value=4).pack()

# 금액 입력
Label(w, text="금액(원)을 입력하세요", bg="lightgray").pack(fill="x")
en = Entry(w)
en.pack()
en.bind("<Return>", calc_money)

# 결과 표시
result = Label(w, text="", fg="blue", font="arial")
result.pack()

w.mainloop()
