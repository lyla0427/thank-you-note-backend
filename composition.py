"""
composition
- 다른 클래스의 일부 메서드를 사용하고 싶지만, ㅅ강속은 하고 싶지 않을 경우
상속의 문제점:
1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다
2. 부모 클래스의 메서드를 오버라이딩하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
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


# Robot이라는 클래스가 있을 때 상속을 받아 다른 동작을 할 수 있게끔 하는 것이 다형성이다


class Korean(Robot):
    def say_hi(self):
        return "안녕"


class English(Robot):
    def say_hi(self):
        return "hi"


class Spanish(Robot):
    def say_hi(self):
        return "hola"


class KoreanCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.add(a, b)


cal = KoreanCal("korea", 2)
print(cal.cal_add(2, 3))
