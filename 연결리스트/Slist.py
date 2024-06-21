class SList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자 객체 생성
            self.item = item  # 노드 항목과 관련된 인스턴스 변수
            self.next = link  # 다음 노드 레퍼런스와 관련된 인스턴스 변수

    def __init__(self):  # 단순 연결 리스트 생성자
        self.head = None  # 아무것도 없음
        self.size = 0  # 항목 수 관련 변수 생성

    def size(self):  # 크기 객체 생성
        return self.size # 항목 수 관련 변수를 size로 지정

    def is_empty(self):
        return self.size == 0  # 항목 수의 값을 0으로 시작함

    def insert_front(self, item):  # 첫 노드로 삽입
        if self.is_empty():  # empty인 경우
            self.head = self.Node(item, None)
        else:  # 그 밖에 경우는
            self.head = self.Node(item, self.head)
        self.size += 1  # 항목 수의 값을 1씩 증가

    def insert_after(self, item, p):  # p 다음에 삽입
        p.next = SList.Node(item, p.next)  # 새 다음 노드가 p 다음 노드가 됨
        self.size += 1  # 항목 수의 값을 1씩 증가

    def delete_front(self):  # 첫 노드 삭제
        if self.is_empty():   # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        else:  # 그 밖에
            self.head = self.head.next  # head가 둘째 노드를 참조
            self.size -= 1  # 항목 수의 값을 1씩 감소

    def delete_after(self, p):  # p 다음 노드 삭제
        if self.is_empty():  # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next  # p다음 노드를 건너 뛰어 연결
        self.size -= 1  # 항목 수 값을 1씩 감소

    def search(self, target):  # target 탐색
        p = self.head  # head로 부터 순차 탐색
        for k in range(self.size):
            if target == p.item: return k  # 탐색 성공
            p = p.next
        return None  # 탐색 실패

    def print_list(self):  # 연결리스트 출력
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next  # 노드들을 순차 탐색


class EmptyError(Exception):  # underflow 시 에러 처리
    pass
