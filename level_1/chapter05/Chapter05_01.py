# class

# 예제 1
class Dog:
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('aa', 1)
b = Dog('bb', 2)
c = Dog('aa', 1)

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print(a.__dict__)
print(b.__dict__)
print('{}: {}, {}: {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)
print()

# 예제2
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest()
print(id(f))
# f.func1() TypeError: SelfTest.func1() takes 0 positional arguments but 1 was given
f.func2()
SelfTest.func1()
# SelfTest.func2() TypeError: SelfTest.func2() missing 1 required positional argument: 'self'
SelfTest.func2(f)
print()

# 예제 3
class Warehouse:
    stock = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock += 1

    def __del__(self):
        Warehouse.stock -= 1

item1 = Warehouse('item1')
item2 = Warehouse('item2')
print(Warehouse.stock)
print(item1.name)
print(item2.name)
print(item1.__dict__)
print(item2.__dict__)
print(Warehouse.__dict__)

del item1
print(Warehouse.__dict__)
print()

# 예제 4
class Dog:
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

a = Dog('a', 3)
b = Dog('b', 10)
print(a.info())
print(a.speak('aaaa'))
print(b.info())
print(b.speak('bbbb'))