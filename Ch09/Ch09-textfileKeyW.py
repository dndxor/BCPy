import os

#선택한 파일 쓰기
fpath = os.getcwd()
infname = input(">생성할 파일명을 입력: ")
fname = fpath + '\\' + infname.strip()
fd = open(fname, 'w')

mlist = []
while True:
    inmember = list(input("> 성명 성별 나이 (입력): ").split())
    if len(inmember) == 0:
        break
    mlist.append(inmember)
print(mlist)

for rec in mlist:
    fd.writelines('\t'.join(rec)+'\n')
fd.close()

