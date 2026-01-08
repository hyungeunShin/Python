# Special Method(Magic Method)
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 일반 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

print()

# 네임드 튜플

from collections import namedtuple

Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)

l_leng2 = sqrt((pt4.x - pt3.x) ** 2 + (pt4.y - pt3.y) ** 2)
print(l_leng2)

print()

Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# Point4 = namedtuple('Point', 'x y x class', rename=False)
Point4 = namedtuple('Point', 'x y x class', rename=True)

print(Point1, Point2, Point3, Point4)

print()

p1 = Point1(x=10, y=20)
p2 = Point2(10, 20)
p3 = Point3(10, y=20)
p4 = Point4(10, 20, 30, 40)

print(p1)
print(p2)
print(p3)
print(p4)
print(Point3(**{'x': 10, 'y': 20}))

print()

print(p1[0] + p2[1])
print(p1.x + p2.y)

x, y = p3
print(x+y)

temp = [10, 20]
# 새로운 객체 생성
p5 = Point1._make(temp)
print(p5)

print()

# 필드 네임 확인
print(p1._fields)

print()

# OrderedDict 반환
print(p1._asdict())

print()

Classes = namedtuple('Classes', ['rank', 'number'])

ranks = ['A', 'B', 'C', 'D']
numbers = [str(n) for n in range(1, 21)]

students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

print()

students2 = [Classes(rank, number)
            for rank in ['A', 'B', 'C', 'D']
                for number in [str(n) for n in range(1, 21)]]

print(len(students2))
print(students2)