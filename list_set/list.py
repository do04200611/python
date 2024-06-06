x , y = input('입력:').split('-')
a = ['abc123', 'def456', 'ghi789']
print(" x,y의 값 추가 전 리스트: ", a)
a.append(x)
a.append(y)
# a.remove('def456')
print("리스트 첫번째 값 출력:", a[1][-3:], a[1])
print("리스트 첫번째 값 출력:", a[1][3:],a[1][:2], a[1][:-2])
print("리스트 특정요소만 출력:", a[2][3:], a[2][:-2])

for i in range(3,6):
    print(i,end= ' ')

print("x,y의 값을 리스트에서 제거 후 출력: " ,"\n 리스트 a: ", a , "\n x값: " ,x, "\n y값: " ,y)


