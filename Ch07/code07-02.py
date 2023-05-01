
# 리스트 사용
alist = ['홍길동', '김유신', 7.8, 6, ['a', 'b']]

for i in range(len(alist)) :
    print("alist[%d] " %i, end='\t')
    print(alist[i], end='\t')
    print(type(alist[i]))

