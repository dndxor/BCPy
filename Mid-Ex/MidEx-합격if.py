scr1 = int(input("과목1 점수? "))
scr2 = int(input("과목2 점수? "))
scr3 = int(input("과목3 점수? "))
scr4 = int(input("과목4 점수? "))
scr5 = int(input("과목5 점수? "))

avg = (scr1 + scr2 + scr3 + scr4 + scr5) / 5
print(avg)

result = "불합격"
if scr1 >= 40 and scr2 >= 40 and scr3 >= 40 and scr4 >= 40 and scr5 >= 40:
    if avg >= 60:
        result = "합격"
print(result)
