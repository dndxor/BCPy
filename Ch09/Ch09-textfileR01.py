## [실습] text 파일 출력 및 원하는 문자열 찾아 10라인 출력하기
 import os

#선택한 파일 출력
fpath = os.getcwd()
infname = input(">출력할 파일명을 입력: ")
fname = fpath + '\\' + infname.strip()

if infname[-3:] == '.py':
    fd = open(fname, 'r', encoding='UTF-8')
else:
    fd = open(fname, 'r')

seq = 0
for line in fd.readlines():
    seq += 1
    print("%3d: %s" %(seq, line), end='')

#문자열 찾기
fd.seek(0)
instr = input("\n>찾을 문자 값: ")
seq = 0
while True:
    line = fd.readline()
    if line == '':
        break
    if instr in line:
        break
    else:
        seq += 1
        spos = fd.tell()    #찾기 전까지의 파일 포인터 번호

#찾은 위치 줄부터 10줄 출력
fd.seek(spos)
lcnt = 0
while lcnt < 10: #10줄만 출력
    line = fd.readline()
    if line == '':
        break
    else:
        seq += 1
        lcnt += 1
        print("%3d: %s" %(seq, line), end='')

fd.close()