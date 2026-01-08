# Special Method(Magic Method)
# https://docs.python.org/3/reference/datamodel.html#special-method-names

print(int)
print(float)

print()

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

print()

n = 10
print(n + 100, n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()

class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    def __ge__(self, x):
        print('__ge__ Method Called')
        if self._price >= x._price:
            return True
        else:
            return False

    def __le__(self, x):
        print('__le__ Method Called')
        if self._price <= x._price:
            return True
        else:
            return False

    def __sub__(self, x):
        print('__sub__ Method Called')
        return self._price - x._price

s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직메소드
print(s1)
print(s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)