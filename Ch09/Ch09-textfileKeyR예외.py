import os

#선택한 파일 쓰기
fpath = os.getcwd()
infname = input(">확인할 파일명을 입력: ")
fname = fpath + '\\' + infname.strip()

#파일 읽어 확인
try:
    a = 3 / 0
    fd = open(fname, 'r')
except BaseException as be:
    print("Error: %s" %be)
except ZeroDivisionError as ze:
    print("Error: %s" %ze)
    #print("!ZeroDivisionError!")
except FileNotFoundError:
    print("파일이 존재하지 않습니다.\n%s" %fname)
else:
    for line in fd.readlines():
        rec = line.split()    #공백으로 분리 후 리스트화
        id, sex, age = rec    #리스트 언팩킹
        print("%10s : %s  %3d" %(id, sex, int(age)))
    fd.close()
finally:
    print("^^ Have a good time!")


