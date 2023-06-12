# Place 배치

from tkinter import *

w = Tk()
w.title("회원 가입")
w.geometry("250x100") # 윈도우 크기("가로x세로") 설정

Label(w, text="이    름").place(x=0, y=0, width=100)
nameEn = Entry(w)
nameEn.place(x=100, y=0)

Label(w, text="전화번호").place(x=0, y=30, width=100)
phoneEn = Entry(w)
phoneEn.place(x=100, y=30)
                                               
Button(w, text="확인", fg="blue").place(x=100, y=60)
                                               
w.mainloop() #이벤트 처리를 위해 대기
