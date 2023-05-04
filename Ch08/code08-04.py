# 회원 가입 여부 확인

members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

search = input("검색할 아이디 입력 : ")
idList = []     # 빈 리스트
for x in members :
    idList.append(x[0])     # 튜플의 아이디(x[0])만 추출해서 리스트에 추가

if search in idList :
    print("가입한 회원입니다.")
else : 
    print("회원이 아닙니다.")

'''
# 코드 줄이기
if search in (x[0] for x in members) :
    print("가입한 회원입니다.")
else :
    print("회원이 아닙니다.")
'''