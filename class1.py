# class1.py

# 클래스 정의

class Person:
    # 초기화 메서드
    def __init__ (self):
        self.name = "default name"
    def print(self):
        peint("My name is {0}" .format(self.name))

# 인스턴스 생성
p1 = Person()
p1.print()
