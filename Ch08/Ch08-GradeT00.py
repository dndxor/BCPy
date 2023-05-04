#등급표 튜플 만들기
grades = (["A+", [100, 95]], ["A", [94, 90]], ["B+", [89, 85]], ["B", [84, 80]],
          ["C+", [79, 75]], ["C", [74, 70]], ["D+", [69, 65]], ["D", [64, 60]],
          ["F", [59, 0]])

#등급표 출력
for grade, zone in grades:
    print(grade, " > ", zone)

#등급표 검색(등급으로 찾기)
ingrade = input("Grade 입력: ")
ingrade = ingrade.upper()
for grade, zone in grades:
    if grade == ingrade:
        print("%s : %d~%d" %(grade, zone[1], zone[0]))

#등급표 검색(점수로 찾기)
inscore = int(input("Score 입력: "))
for grade, zone in grades:
    if inscore >= zone[1] and inscore <= zone[0]:
        print("%d : %s" %(inscore, grade))