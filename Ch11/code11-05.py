# Grid 배치

from tkinter import *

w = Tk()
w.title("회원 가입")

Label(w, text="이    름").grid(row=0, column=0)
nameEn = Entry(w)
nameEn.grid(row=0, column=1)

Label(w, text="전화번호").grid(row=1, column=0)
phoneEn = Entry(w)
phoneEn.grid(row=1, column=1)
                                               
Button(w, text="확인", fg="blue").grid(row=2, column=0, columnspan=2)
                                               
w.mainloop() #이벤트 처리를 위해 대기
