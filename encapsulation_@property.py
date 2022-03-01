"""
@property
- 인스턴스 변수 값을 사용해서 적절한 값을 고 보내고 싶을 때
- 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:
    population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # private 변수가 되는 것. 상속 받을 때도 없어진다. 클래스 자체에서만 사용할 수 있음.
        Robot.population += 1

    @property  # 인스턴스 변수 값을 사용해서 적절한 값을 고 보내고 싶을 때
    def name(self):
        return f"lee {self.__name}"

    @property  # 인스턴스 변수 값에 대한 유효성 검사 및 수정
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid age range")
        self.__age = new_age

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


ss = Robot("yss", 8)
print(ss.age)  # 8, 은닉된 변수에 접근이 가능하다!
ss.age = 2  # @setattr를 쓰기 전까지는 AttributeError: can't set attribute가 나온다. 하지만 @setattr를 설정하면 해당 property (age)의 set attribute를 찾고 찾게 되면 성공!
# @setattr를 쓰는 이유는 해당 attribute에서 validation을 할 수 있기 때문. 즉, 개발자가 원하는 변수의 범위를 지정하거나 하는 등의 규칙을 설정할 수 있다는 것.
ss.age += 1
print(ss.age)
print(ss.name)
