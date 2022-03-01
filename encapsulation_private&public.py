"""
public vs private

namespace 보호, 접급할 수 없게 하기 위해 쓰이는 방법이 private
"""


class Robot:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private 변수가 되는 것. 상속 받을 때도 없어진다. 클래스 자체에서만 사용할 수 있음.
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


ss = Robot("yss", 8)
print(ss.__age)  # AttributeError: 'Robot' object has no attribute 'age'
