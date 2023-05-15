## [실습] text 파일 출력 및 원하는 문자열 찾기
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
for line in fd.readlines():
    seq += 1
    if instr in line:
        print("%3d: %s" %(seq, line), end='')
        print("     "+ " "*line.index(instr)+"^")

fd.close()