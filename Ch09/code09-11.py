# 회원 정보 등록하기

print("아이디와 비밀 번호를 등록하세요.")
inid = input("아이디 : ")
inpwd = input("비밀번호 : ")

with open("c:/python/login.txt", "a") as f : # 파일 끝에 추가("a" 모드)
    num = 0
    f.writelines(inid + " " + inpwd + "\n")

print("등록되었습니다.")
