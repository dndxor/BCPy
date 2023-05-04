members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))
grades = {"A+": [100, 95], "A": [90], "B+": [85], "B": [80], "C+": [75],
          "C": [70], "D+": [65], "D": [60], "F": [0]}

ingrade = input("등급 입력: ")
if ingrade in grades.keys() :
    print(grades[ingrade])

inscore = int(input("점수 입력: "))
if inscore in grades.values() :
    print("점수가 존재함.")

for x, y in grades.items() :
    if inscore in y :
        print(x, grades[x])
