ch = '*'

def print_line(n):
    print(ch*n)

def print_title(s):
    slen = len(s)
    print_line(slen)
    print(s)
    print_line(slen)