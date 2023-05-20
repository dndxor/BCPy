##[과제-초안] 회원 아이디 검색을 재귀 호출로 해결 : Ch10-BinarySearch00.py
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

scnt = 0  #search counter
def Bi_search(search, members, start, end):  #재귀 호출 함수
    return -1  #찾기 실패 시

search = input(">아이디 입력 : ")
result = -1     #찾은 위치 값의 초기화(number 변수를 대체)
start = 0       # 범위의 시작과 마지막 설정
end = len(members)   #index 값이므로 -1
result = Bi_search(search, members, start, end)  #찾은 값에 대한 index 값을 반환 받는다.
if result == -1:
    print("Not found!")
else:
    print(">>Index : %3d, Value : %s" %(result, members[result][0]))
    print(">>Count of search : %d" %scnt)