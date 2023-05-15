fname = input(">출력할 파일명을 입력: ")
fd = open(fname, 'r', encoding='UTF-8')

seq = 0
for line in fd.readlines():    #한 줄씩 인출
    seq += 1
    print("%3d: %s" %(seq, line), end='')

fd.clos()