org = input("원본 파일명 : ")
new = input("복사할 파일명 : ")

try :
    orgfile = open(org, "rb")   # 바이트 단위로 파일 읽기
except :
    print("파일을 확인하세요.")
else :
    data = orgfile.read()
    orgfile.close()
   
    with open(new, "wb") as newfile : # 바이트 단위로 파일 쓰기
       newfile.write(data)
    print("파일이 복사되었습니다.")
    
