class Student:
   a = [1, 5, 4, 6, 8, 11, 3, 12]

   #a에서 짝수만 선택하여 리스트로 반환
   even = list(filter(lambda x: (x % 2 == 0), a))

   # a에서 홀수만 선택하여 리스트로 반환
   other_even = list(filter(lambda x: (x % 2 == 1), a))
   #a에서 짝수만 있는 리스트 반환
   print("각 숫자를 짝수로 만들기 "+str(even))
   #a에서 홀수만 있는 리스트 반환
   print("각 숫자를 홀수로 만들기 "+str(other_even))


   ten_times = list(map(lambda x: x * 10, a)) # 원소 값의 10배로 만들어서 리스트 반환
   print("각 숫자를 10배로 만들기 "+str(ten_times)) # 결과 출력

   b = [[0, 1, 8], [7, 2, 2], [5, 3, 10], [1, 4, 5]]

   b.sort(key=lambda x: x[2])  # 0번째 원소의 마지막 숫자를 기준으로 정렬
   print("2번째 원소의 마지막 숫자를 기준으로 정렬 " + str(b))  # 0번째 원소의 마지막 숫자를 기준으로 정렬 결과 출력

   b.sort(key = lambda  x: x[1]) # 1번째 원소의 마지막 숫자를 기준으로 정렬
   print("1번째 원소의 마지막 숫자를 기준으로 정렬 "+str(b)) # 1번째 원소의 마지막 숫자를 기준으로 정렬 결과 출력

   b.sort(key=lambda x: x[0]) #0번째 원소의 마지막 숫자를 기준으로 정렬
   print("0번째 원소의 마지막 숫자를 기준으로 정렬 "+str(b))# 0번째 원소의 마지막 숫자를 기준으로 정렬 결과 출력
