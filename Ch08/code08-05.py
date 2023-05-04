members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

memberId = ''
num = 0

for x, y in members :   # x:아이디, y:점수
    if y > num :    # 점수 비교
        memberId = x
        num = y
        
print("만족도 점수가 가장 높은 회원은 %s, 점수는 %d입니다." % (memberId, num))



'''
# 최대값만 찾기
top = max(x[1] for x in member)
'''
