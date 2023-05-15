
fd = open("poem.txt", "r")  #file open  > fd 객체 생성
print(fd.read())            #Read file  > 전체 읽기
#print(fd.readline())       #Read file > 한 줄 읽기
#print(fd.readlines())      #Read file > 한 줄씩 전체 읽어 리스트화
fd.close()                  #close file

with open("poem.txt", "r") as fd:   #file open  > fd 객체 생성
    print(fd.read())            #Read file  > 전체 읽기
    fd.close()                  #close file

fd = open("poem.txt", "r")  #file open
for x in fd.read():                #Read file > 줄 단위로 읽어 x에 넘기기
    print(x, end='')
fd.close()                  #close file

fd = open("poem.txt", "r")  #file open
x = ' '
while x != '':
    x = fd.readline()       #Read file > 줄 단위로 읽어 x에 넘기기
    print(x, end='')
fd.close()                  #close file           #close file

fd = open("poem.txt", "r")  #file open
for x in fd.readlines():    #Read file > 전체를 리스트로 만들어, 줄 단위로 x에 넘기기
    print(x, end='')
fd.close()                  #close file
