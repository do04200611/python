class Student:
    def __init__(self, name, id): #Student 객체 생성자
        self.name = name # 인스턴스 변수
        self.id = id # 인스턴스 변수
    def get_name(self): # 객체의 name을 반환하는 메소드
        return self.name # name 값 반환
    def get_id(self): # 객체의 id를 반환하는 메소드
        return self.id #id 값 반환

best = Student('Lee', 101) #id name 값을 best 변수에 저장
print(best.get_name()) # name 값 출력
print(best.get_id()) # id 값 출력
