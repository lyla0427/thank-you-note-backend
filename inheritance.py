"""
[클래스 상속]
1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. super()
5. python의 모든 클래스는 object 클래스를 상속한다: 모든 것은 객체이다

Myclass.mro() --> 상속 관계를 보여준다.
"""


class Robot:  # 사실 Robot(object)를 상속받고 있다!
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        return f"my name is {self.name}"

    def add(self, a, b):
        return a + b

    def die(self):
        Robot.population -= 1
        return f"{self.name} dead {Robot.population} working"

    @classmethod
    def how_many(cls):
        return f"we have {cls.population} robots"

    @staticmethod
    def this_is_robot_class():
        return "yay"

    def __str__(self):
        return f"{self.name}"

    def __call__(self):
        return f"{self.name} is called. 이거 없으면 not callable 에러 남"


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name)  # 로봇이라는 클래스 그 자체를 의미한다
        self.age = age  # name을 할당해줄 필요가 없고 새로 추가한 age만 할당해준다

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    def say_hi(self):
        return "hi"

    def call_flexible(self, a, b):
        print(super().say_hi())
        print(self.say_hi())
        return (
            self.cal_mul(a, b) + self.add(a, b) + super().add(a, b)
        )  # 오버라이딩을 하지 않아도 super를 사용할 수 있음

    @classmethod
    def hello_apple(cls):
        print(f"{cls}")


siri = Siri("siri", 1)

# 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
# 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
print(siri)
print(siri.this_is_robot_class())
print(siri.add(1, 3))

# 3 메서드 오버라이딩
print(siri.call_me())
print(siri.cal_mul(1, 5))
print(siri.a)
Siri.hello_apple()
print(siri.this_is_robot_class())
print(Robot.population)
print(siri.population)

# 4 super()
print(siri.age)
print(siri.name)
print(siri.call_flexible(2, 3))

# 5 python의 모든 클래스는 object 클래스를 상속한다: 모든 것은 객체이다
print(
    Siri.mro()
)  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

print(object)  # <class 'object'>
print(
    dir(object)
)  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print(object.__name__)  # object
print(int.mro())  # [<class 'int'>, <class 'object'>]
"""
파이썬 내부에 뭔가 많기 때문에 다른 언어에 비해 느리다는 소리를 듣는 것이지만 그만큼 강력하고 다이나믹 할 수 있는 것.
때문에 빠르게 제품을 생산할 수 있고 과학적인 통계와 계산에 강한것이다.
"""


# 다중 상속: 안티 패턴이지만 가능함. 부품 조립이라고 생각하면 됨 (mixin)


class A:  # 부품 1
    pass


class B:  # 부품 2
    pass


class C:  # 부품 3
    pass


class D(A, B, C):  # 자동차
    pass


print(
    D.mro()
)  # [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
# C의 함수를 A가 오버라이딩 할 수 도 있으니 다중상속을 하면 유지보수가 어렵다
