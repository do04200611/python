num = int(input()) # num의 값을 입력 받음

for i in range(1,10) : # 입력 받은 값 만큼 실행
    sum = num*i # 구구단을 할 값을 변수 sum에 저장
    print(num,'*',i,'=',sum) # 구구단 출력

# 또다른 버전

num = int(input()) # num의 값을 입력 받음

for i in range(1,10) : # 입력 받은 값 만큼 실행
    sum = num*i # 구구단을 할 값을 변수 sum에 저장
    print("{0} x {1} = {2:>2}".format(num, i, num * i))  # 위 코드와 동일함.
