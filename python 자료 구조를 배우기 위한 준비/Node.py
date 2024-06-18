class Node:
   def __init__(self, name, left=None, right=None): # 섬 생성자
      self.name = name
      self.left = left
      self.right = right

def map(): # 지도 만들기
   n1 = Node('H')  # n1의 Node를 H로 지정
   n2 = Node('F')  # n2의 Node를 F로 지정
   n3 = Node('S') # n3의 Node를 S로 지정
   n4 = Node('U')  # n4의 Node를 U로 지정
   n5 = Node('E')  # n5의 Node를 E로 지정
   n6 = Node('Z')  # n6의 Node를 Z로 지정
   n7 = Node('K')  # n7의 Node를 K로 지정
   n8 = Node('N')  # n8의 Node를 N로 지정
   n9 = Node('A')  # n9의 Node를 A로 지정
   n10 = Node('Y')  # n10의 Node를 Y로 지정
   n11 = Node('T')  # n11의 Node를 T로 지정

   n1.left = n2  # n1의 왼쪽은 n2(F)로 지정
   n1.right = n3  # n1의 오른쪽은 n3(S)로 지정
   n2.left = n4  # n2의 왼쪽은 n4(U)로 지정
   n2.right = n5  # n2의 오른쪽은 n5(E)로 지정
   n3.left = n6  # n3의 왼쪽은 n5(Z)로 지정
   n3.right = n7  # n3의 오른쪽은 n7(K)로 지정
   n4.left = n8  # n4의 왼쪽은 n8(N)로 지정
   n5.left = n9  # n5의 왼쪽은 n9(A)로 지정
   n7.right = n10  # n7의 오른쪽은 n10(Y)로 지정
   n9.right = n11  # n9의 오른쪽은 n11(T)로 지정

   return n1 #시작섬 반환

def A_course(n):  # A-코스
   if n != None:  # n이 None이 아니면
      print(n.name, '->', end='')  # 섬 n 방문
      A_course(n.left)  # n의 왼쪽 진행
      A_course(n.right) # n의 오른쪽 진행

def B_course(n):  # B-코스
   if n != None:  # n이 None이 아니면
      B_course(n.left)  # n의 왼쪽 진행
      print(n.name, '->', end='')  # 섬 n 방문
      B_course(n.right)  # n 오른쪽 진행

def C_course(n):  # C-코스 
   if n != None:  # n이 None이 아니면  
      C_course(n.left)  # n의 왼쪽 진행 
      C_course(n.right) # n의 오른쪽 진행
      print(n.name, '->', end='')  # 섬 n 방문

start = map()  # 시작섬을 n1로
print('A-코스:\t', end='')  # A코스 대로 섬 방문 진행
A_course(start)  # A 코스 진행 시작

print('\nB=코스:\t', end='')  # B 코스 대로 섬 방문 진행
B_course(start)  # B 코스 시작
 
print('\nC= 코스:\t', end='')  # C코스 대로 섬방문 진행
C_course(start) # C코스 시작
