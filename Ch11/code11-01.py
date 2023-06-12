from tkinter import *

w = Tk()    # 기본 윈도우 만들기

lb = Label(w, text = "이름을 입력하세요.")   # 레이블 만들기
en = Entry(w)    # 엔트리(입력 상자) 만들기
bt = Button(w, text = "확인")  # 버튼 만들기

lb.pack()    # 위젯 표시하기
en.pack()
bt.pack()

w.mainloop()    # 이벤트 처리를 위해 대기
