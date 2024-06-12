num = int(input())
for i in range(num):
    a, b = list(map(int, input().split()))
    sum = a+b
    print("Case #"+str(i+1)+": "+str(sum))
