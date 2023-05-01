'''
# 변수 사용
b1 = 234
b2 = 82
b3 = 128
b4 = 50
b5 = 155

total = b1 + b2 + b3 + b4 + b5
print("판매수량 합계 = ", total)
print("판매수량 평균 = ", total / 5)
'''

# 리스트 사용
books = [234, 82, 128, 50, 155]
total = 0

for x in books :
    total += x
print("판매수량 합계 = ", total)
print("판매수량 평균 = ", total / len(books))


