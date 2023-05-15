# 영어 단어 사전 만들기

sentence = ""   # 입력한 문장
words = []      # 입력한 문장을 분리해 두는 단어 리스트
dic = []        # 사전 리스트
print("문장의 단어를 등록합니다(종료는 0 입력).")
while True :
    sentence = input("문장 입력 : ")
    if sentence == '0' :
        break
    words = sentence.split()    # 입력한 문장을 단어 리스트에 분리해서 저장
    for x in words :
        if x not in dic :       # 새로운 단어인지 먼저 검사한 후 등록
            dic.append(x)
    
print("*****단어 사전*****")
for x in sorted(dic):   # 리스트를 정렬해서 출력
    print(x)

