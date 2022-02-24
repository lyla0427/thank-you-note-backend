class Robot:
    """
    __method__는 매직 매서드. 각 역할이 있는 파이썬의 내장 메서드
    """

    # 클래스 변수 : 인스턴스끼리 공유하는 변수
    population = 0

    def __init__(self, name, serial_num, *num):
        self.name = name
        self.serial_num = serial_num
        self.num = num
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

    # 굳이 self나 cls를 써서 함수를 만들어야 하나?
    @staticmethod
    def this_is_robot_class():
        return "yay"

    def __str__(self):
        return "사실 프린트는 __str__이지롱"

    def __call__(self):
        return f"{self.name} is called. 이거 없으면 not callable 에러 남"


droid = Robot("lyla", 223)
print(droid.say_hi())

print(dir(droid))  # 어떤 클래스로 만들어져 있는지 확인할 수 있음
print(
    droid
)  # 프린트로 객체를 찍는 다는 것은 객체를 문자열화 시키는 것임. 이건 __str__ 메서드를 활용해서 가능하게 됨 (<method-wrapper '__str__' of Robot object at 0x7f7fce190f40>)
print(Robot.__str__(droid))

print(
    droid()
)  # 괄호는 callable하다는 것. __call__ 메서드를 활용함. 파이썬의 모든 것은 객체이기 때문에 __call__ 매직매서드를 활용하여 호출 가능하게 해보자
