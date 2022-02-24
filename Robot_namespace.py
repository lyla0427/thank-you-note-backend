class Robot:
    """
    namespace : 개체를 구분할 수 있는 범위,
    A namespace is a declarative region that provides a scope to the identifiers (the names of types, functions, variables, etc) inside it. Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
    클래스 변수 : 인스턴스끼리 공유하는 변수
    """

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
print(Robot.__dict__)
