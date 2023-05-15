try :
    f = open("c:/python/login.txt", "r") 
except :
    print("파일을 확인하세요.")
else :
    inid = input("아이디 입력 : ")
    inpwd = input("비밀번호 입력 : ")
    result = 0  # 아이디와 비밀번호를 찾으면 1로 변경
    
    for data in f :
        data = data.rstrip() # 읽은 문자열의 오른쪽에 있는 '\n'을 제거
        items = data.split() # 공백을 기준으로 잘라서 리스트에 저장(['id', 'pwd'])
        
        if items[0] == inid and items[1] == inpwd : # 값이 일치하면 반복 종료
            print("안녕하세요, %s." % inid)
            result = 1  # 일치하는 아이디와 비밀번호를 찾음
            break

    f.close()
    if result == 0 : # 일치하는 아이디와 비밀번호가 없음
        print("아이디와 비밀번호를 확인하세요.")

    
    
