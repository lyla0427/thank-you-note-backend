class Robot:
    """
    메롱
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


droid = Robot("lyla", 223)
print(Robot.this_is_robot_class())
print(droid.this_is_robot_class())
