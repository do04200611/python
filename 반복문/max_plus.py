num = int(input()) # num의 값을 입력 받음
sum =1

for i in range(1,num) : # 입력 받은 값 만큼 실행
    sum += i+1 # num 까지의  값을 합쳐서 변수 sum에 저장

print(int(sum))  # sum 출력
