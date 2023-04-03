score = int(input("점수를 입력하세요 : "))
grade = ''

##복잡도 : (1+2+3+4+4)/5 = 2.8
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=  70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("등급은 ", grade)

##복잡도 : (1+4+7+10+10)/5 = 6.4
if score >= 90:
    grade = 'A'
elif score < 90 and score >= 80:
    grade = 'B'
elif score < 80 and score >=  70:
    grade = 'C'
elif score < 70 and score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("등급은 ", grade)