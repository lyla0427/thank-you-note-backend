class Calculator:
    # 생성자 constructor: 메모리에 올라오는 순간 (인스턴스를 만들때) 즉시 실행이 되는 함수
    def __init__(self, a, b):  # 클래스로 하나의 인스턴스를 만들었을 때 그 인스턴스를 지칭하는 이름
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


my_calc1 = Calculator(1, 2)
my_calc2 = Calculator(4, 6)
print(my_calc1.add())
print(my_calc2.add())
