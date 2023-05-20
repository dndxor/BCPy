members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
          ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song', 75))

search = input("아이디 입력 : ")
number = -1     # 만족도 점수의 초기화
start = 0       # 범위의 시작과 마지막 설정
end = len(members)   #index 값이므로 -1
mid = (start + end) // 2  # 가운데 항목을 첫 번째 검색 위치로 설정

while start < end :
    if search == members[mid][0] :  # 찾는 아이디가 있으면 점수를 저장하고 반복 종료
        number = members[mid][1]
        break
    else :
        if start == (end - 1) : # 검색 범위를 줄일 수 없음(=찾는 값이 없음)
            break
        elif search > members[mid][0] :   
            start = mid + 1   # 검색 범위를 뒤쪽 반으로 줄이기
            mid = (start + end) // 2
        else :                  
            end = mid  # 검색 범위를 앞쪽 반으로 줄이기
            mid = (start + end) // 2

if number > -1 :
    print(search, number)
else :
    print("찾는 회원이 없습니다.")

    




