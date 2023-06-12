# Pack 배치

from tkinter import *

w = Tk()        # 윈도우 제목
w.title("회원 가입")

Label(w, text="이    름").pack()
nameEn = Entry(w)
nameEn.pack()

Label(w, text="전화번호").pack()
phoneEn = Entry(w)
phoneEn.pack()

Button(w, text="확인", fg="blue").pack()
 
w.mainloop() 
