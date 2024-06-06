num_list = list(map(int, input().split()))

num_list.pop()
print("배열 마지막 요소 제거 후"+ str(num_list))

new_num_list = num_list.pop(2)
print("2번째 값 제거 후 결과: "+str(num_list))

new_num_list = num_list.pop(-2)
print("마지막 2번째 값 제거 후 결과: "+str(num_list))

new_num_list = num_list.count(2)
print("값이 저장된 요소 개수 출력: "+ str(new_num_list)+"\n"+str(num_list))

new_num_list = num_list.index(2)
print("값이 저장된 요소 위치 출력: "+ str(new_num_list))

new_num_list = num_list.reverse()
print("리스트 거꾸로 정렬 결과 출력: "+ str(num_list))

num_list.sort()
print("배열 값 정렬 후"+ str(num_list))


print("리스트 복사 전 결과 출력: "+str(new_num_list))
new_num_list = num_list.copy()
print("리스트 복사 한 결과 출력: "+str(new_num_list))
