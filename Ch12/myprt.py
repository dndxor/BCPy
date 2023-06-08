#나 모듈
ch = '#'

def prt_line(n):
    print('#'*n)

def prt_title(str):
    slen = len(str)
    prt_line(slen)
    print(str)
    prt_line(slen)