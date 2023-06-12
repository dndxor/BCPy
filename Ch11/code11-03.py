from tkinter import *

w = Tk()

# 레이블 만들기
Label(w, text="좋아하는 음악을 하나만 선택하세요.",
      bg="gray", fg="yellow", width=30).pack()

# 라디오버튼 만들기
x = IntVar() # 정수형 객체 생성(라디오버튼에서 선택한 값을 저장하기 위한 변수)

Radiobutton(w, text="가요", variable=x, value=1).pack()
Radiobutton(w, text="팝송", variable=x, value=2).pack()
Radiobutton(w, text="클래식", variable=x, value=3).pack()
Radiobutton(w, text="뉴에이지", variable=x, value=4).pack()

# 레이블 만들기
Label(w, text="선호도를 점수로 표시하세요.",
      bg="gray", fg="yellow", width=30).pack()

# 슬라이더 만들기
y = IntVar()
Scale(w, variable=y, orient="horizontal", length=200).pack() # 슬라이더 길이(length)의 기본값=100

w.mainloop()

