from tkinter import *

w = Tk()

x = DoubleVar() # 실수형 객체
print(x.get())  # x의 값을 쉘에 출력

x.set(123.45)   # x의 값을 변경
print(x.get())  # 변경된 값을 쉘에 출력

w.mainloop()

