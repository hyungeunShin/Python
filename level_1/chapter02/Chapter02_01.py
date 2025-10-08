# 데이터 타입
str1 = 'Python'
str2 = "Java"
bool = False
list = [str1, str2]
dict = {
    "name": "홍길동",
    "version": 1.0
}
tuple1 = (1, 2, 3)
tuple2 = 4, 5, 6
set = {1, 2, 3, 3}
print(list)
print(dict)
print(tuple1)
print(tuple2)
print(set)
print()

print(type(str1))
print(type(bool))
print(type(list))
print(type(dict))
print(type(tuple1))
print(type(tuple2))
print(type(set))
print()

# 정수
big_int = 99999999999999999999999999999999999999999999999999
print(big_int)
print(type(big_int))

# 실수
float_v = 0.33333333333333333333333333333
print(float_v)
print()

# 연산
print(9 / 4)
print(9 // 4)
print(9 % 4)
print(1 + 1.0)
print()

# 형 변환
a = 3.
b = 6
c = .7
d = 12.7
print(type(a))
print(int(a), float(b), int(c), int(d))
print(int(True)) # True: 1, False: 0
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))
print()

# 수치 연산
print(abs(-2))
print(pow(2, 3))
print(2 ** 3)
x, y = divmod(100, 8)
print(x, y)
print()

# 외부 모듈
import math

print(math.ceil(5.1))
print(math.floor(5.1))
print(math.pi)