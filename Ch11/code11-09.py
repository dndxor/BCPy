#사칙연산 계산기

from tkinter import *

def f_add() :   # 덧셈 버튼 클릭 이벤트 처리
    num1 = float(e1.get())
    num2 = float(e2.get())
    eResult.delete(0, END) #기존에 표시한 결과를 모두 지우기
    eResult.insert(0, "%s" % (num1+num2)) # 계산 결과를 표시
    
def f_sub() :   # 뺄셈 버튼 클릭 이벤트 처리
    num1 = float(e1.get())
    num2 = float(e2.get())
    eResult.delete(0, END)
    eResult.insert(0, "%s" % (num1-num2))

def f_mul() :   # 곱셈 버튼 클릭 이벤트 처리
    num1 = float(e1.get())
    num2 = float(e2.get())
    eResult.delete(0, END)
    eResult.insert(0, "%s" % (num1*num2))

def f_div() :   # 나눗셈 버튼 클릭 이벤트 처리
    num1 = float(e1.get())
    num2 = float(e2.get())
    eResult.delete(0, END)
    eResult.insert(0, "%.6f" % (num1/num2)) #자릿수를 소수점 이하 6자리로 표시

w = Tk()
w.title("사칙연산기")
l1 = Label(w, text="숫자1")
l2 = Label(w, text="숫자2")
e1 = Entry(w, width=10)
e2 = Entry(w, width=10)
bAdd = Button(w, text="+", width=4, command=f_add)
bSub = Button(w, text="-", width=4, command=f_sub)
bMul = Button(w, text="*", width=4, command=f_mul)
bDiv = Button(w, text="/", width=4, command=f_div)
eResult = Entry(w) # 결과를 표시하는 엔트리
 
l1.grid(row=0, column=0, columnspan=2)
e1.grid(row=0, column=2, columnspan=2)
l2.grid(row=1, column=0, columnspan=2)
e2.grid(row=1, column=2, columnspan=2)
bAdd.grid(row=2, column=0)
bSub.grid(row=2, column=1)
bMul.grid(row=2, column=2)
bDiv.grid(row=2, column=3)
eResult.grid(row=3, column=0, columnspan=4)

w.mainloop() #이벤트 처리를 위해 대기
