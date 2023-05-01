## 1차원 리스트 출력 함수 prt_list() 만들기
alist = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]

def prt_list(alist, reverse=False):  #출력 순서 기본값은 오름차순
    if reverse == False:
        for i in range(len(alist)):
            print(alist[i], end=' ')
    else:
        for i in range(len(alist)-1, 0-1, -1):
            print(alist[i], end=' ')
    print()

prt_list(alist)
prt_list(alist, reverse=True)