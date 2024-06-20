class SList:
   class Node:
      def __init__(self, item, link): 
         self.item = item  # 노드 항목과 관련된 인스턴스 변수
         self.next = link # 다음 노드 레퍼런스와 관련된 인스턴스 변수

   def __init__(self):
      self.head = None # 아무것도 없음
      self.size = 0 # size는 0으로 지정

   def size(self): return self.size  # 값을 지정할 메소드를 생성 후, 반환 값은 size로 지정 
   def is_empty(self): return self.size == 0  # 텅 비어있을 때, 반환 값에 크기는 0으로 지정

   def insert_front(self, item):
      if self.is_empty():  # empty인 경우 에러 처리
         self.head = self.Node(item, None)
      else:  # 그 밖에 경우 에는
         self.head = self.Node(item, self.head)
      self.size += 1  #  크기를 1씩 증가

   def insert_after(self, item, p):
      p.next = self.Node(item, p.next)  # 새 노드가 p 다음 노드가 됨
      self.size += 1  # size의 값 1 증가

   def delete_front(self):  # 첫 노드 삭제
      if self.is_empty(): 
         raise EmptyError('Underflow')
      else:
         self.head = self.head.next
         self.size -= 1  # 크기를 1씩 감소

   def delete_after(self, p):  # p 다음 노드 삭제
      if self.is_empty():
         raise EmptyError('Underflow')
      t = p.next
      p.next = t.next
      self.size -= 1  # 크기를 1씩 감소

   def search(self, target):  # target 탐색
      p = self.head
      for k in range(self.size):
         if target == p.item: return k
         p = p.next
      return None  # 탐색 실패

   def print_list(self):
      p = self.head 
      while p:
         if p.next != None:
            print(p.item, '->', end='')
         else: # 그 밖에 경우는
            print(p.item)
         p = p.next  # 노드들을 순차 탐색
class EmptyError(Exception):  # underflow시 에러 처리
    pass   # 에러를 발생시키지 않음



