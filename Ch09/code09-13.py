try :
    f = open("poem.txt", "r+", encoding = "utf-8") 
except :
    print("파일을 확인하세요.")     # 파일 읽기 오류가 발생하면 실행
else :
    text = f.read()     # 파일 읽기
    print(text)

    org = input("\n찾을 내용 : ")
    new = input("바꿀 내용 : ")

    print("%d 번을 모두 바꿉니다." % text.count(org))
    text = text.replace(org, new)
    f.seek(0)           # 파일 포인터를 처음으로 이동
    f.write(text)       # 파일 수정
    f.close()

    
    
