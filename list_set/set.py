num_list = list(map(int, input().split()))

new_set = set(num_list)
print("리스트를 세트로 변환한 결과"+str(new_set))


print("세트의 요소들 합계: "+str(sum(num_list)))

other_set = {1,2,3}
print("세트에 값을 추가 전 결과"+str(other_set))

other_set.add(5)
print("세트에 값을 추가한 결과"+str(other_set))

other_set.add(25)
new_otherset = other_set.pop()
print("세트에 값을 제거 한 결과: "+str(new_otherset)+ "\n"+str(other_set))

other_set.remove(25)
print("세트에 값을 제거 한 결과: "+str(other_set))

other_set.update({1,2,3, 50, 100})
print("세트에 값을 업데이트 한 결과: "+str(other_set))

print("세트 요소 합계: "+str(sum(other_set)))
print("세트 요소 최댓값: "+str(max(other_set)))
print("세트 요소 최소값: "+str(min(other_set)))
print("세트 요소 길이 값: "+str(len(other_set)))
print("세트 요소 정렬 결과: "+str(sorted(other_set)))

other_set.clear()
print("세트 요소 모두 삭제한 결과: "+str(other_set))
