from tkinter import *

w = Tk()

lb = Label(w, text="이름을 입력하세요.", bg="gray", fg="white")   # 레이블 생성
en = Entry(w, border = 5, cursor="circle")                           # 엔트리 생성
bt = Button(w, text="확인")            # 버튼 생성
bt.config(font="Tahoma", fg="blue")     # 버튼 속성 변경

lb.pack()
en.pack()
bt.pack()

'''
# 참고 : 위젯의 속성 변경하기
img = PhotoImage(file="coffee.gif")
lb.config(image=img)
bt.config(text="커피 쿠폰 당첨")
'''

w.mainloop()
