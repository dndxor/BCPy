# D-Day 계산기

from tkinter import *
from mydays import *

def f_click() :
    days, hours = calc_days(enDday.get())
    lbResult.config(text="D- {0}일 {1}시간".format(days, hours))

w = Tk()
w.title('D-Day 계산기')

yy, mm, dd = get_today()
Label(w, text="오늘 날짜", width=20).grid(row=0, column=0, pady=5)
lbToday = Label(w, text="{0}년 {1}월 {2}일".format(yy, mm, dd))
lbToday.grid(row=0, column=1)

Label(w, text="D-Day (예)20210301").grid(row=1, column=0, pady=5)
enDday = Entry(w)
enDday.grid(row=1, column=1)

btCalc = Button(w, text="계산하기", width=20, command=f_click)
btCalc.grid(row=2, column=0, columnspan=2, pady=5)

lbResult = Label(w, text="D-", font=("arial",15), fg="red")
lbResult.grid(row=3, column=0, columnspan=2, pady=5)

w.mainloop()
