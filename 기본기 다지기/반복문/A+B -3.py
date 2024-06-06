num = int(input()) # a의 값을 입력 받음

for i in range(a) : # 입력 받은 값 만큼 실행
    num2, num3 = list(map(int, input().split())) # 두 개의 숫자 입력 받음
    sum = num2+num3 # 두 값을 합쳐서 변수 sum에 저장
    print(sum) # sum 값 출력
