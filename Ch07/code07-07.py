# 점수를 입력받아 평균을 출력
numbers = []

for _ in range(5):
    numbers.append(int(input("점수 입력 : ")))
    
print("평균 =", sum(numbers) / len(numbers))
