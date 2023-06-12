#그림판 만들기

from tkinter import *

def f_thick() :
    global penWidth
    penWidth = 10

def f_thin() :
    global penWidth
    penWidth = 5
    
def f_clear() :
    cv.delete("all")

def f_exit() :
    w.destroy()

def f_draw(event) :
    global penWidth
    x = event.x  # 마우스의 현재 좌표
    y = event.y
    cv.create_oval(x, y, x+1, y+1, width=penWidth) # width는 타원의 선 두께
    
penWidth = 5    # 펜 두께 설정
w = Tk()
w.title("그림판")
cv = Canvas(w, width=800, height=600, background="lightblue")
cv.pack()
cv.bind("<B1-Motion>", f_draw) #마우스 왼쪽 버튼 클릭을 함수 draw에 연결

fr = Frame(w)
fr.pack()  # 프레임을 윈도우에 추가

bThick = Button(fr, text="두껍게", font="Tahoma", command=f_thick)
bThin = Button(fr, text="가늘게", font="Tahoma", command=f_thin)
bClear = Button(fr, text="지우기", font="Tahoma", command=f_clear)
bExit = Button(fr, text="나가기", font="Tahoma", command=f_exit)
bThick.grid(row=0, column=0)
bThin.grid(row=0, column=1)
bClear.grid(row=0, column=2)
bExit.grid(row=0, column=3)

w.mainloop()
