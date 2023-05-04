members = {'choi':93, 'han':50, 'jung':92, 'kang':68, 'kim':80,
           'lee':90, 'moon':65, 'na':100, 'park':75, 'song':75}

total = 0
for x in members.values() : # 항목의 값을 모두 추출하고, x에 하나씩 대입하는 반복문
    total += x

print("회원 점수 평균 =", total / len(members))
