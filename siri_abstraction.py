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


print(Robot.population)
Jarvis = Robot("Jarvis", 2929, [1, 2])
print(Robot.population)
print(Jarvis.say_hi())
print(Jarvis.add(2, 3))
print(Jarvis.die())
print(Robot.population)
print(Robot.how_many())

print(dir(Jarvis))
print(Robot.__doc__)
print(Jarvis.__class__)
