import random
# 리스트 사용
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    #중복방지 난수 발생용 씨드
strike = 0; ball = 0
randarr = []        #3자리 난수 리스트
guesarr = [0, 0, 0] #3자리 추측 리스트
bcnt = 0            #시도 횟수

randarr = random.sample(arr, 3)
#print(randarr)
while True :    #맞추기 게임 시도 반복
    #변수 초기화

    #3개값 숫자로 입력 받아 각 자리값을 분리하기(3개로)
    innum = int(input(">>정수(1~999; esc 00) 입력: "))  #추측값(정수) 입력

    #각 자리값이 정답과 맞는지 확인(존재 및 위치 정확성)



    print("[%d] %d Strike  %d Ball " %(bcnt, strike, ball))     #시도 결과 출력
    #3s이면 게임 종료
    if strike == 3 :
        break
