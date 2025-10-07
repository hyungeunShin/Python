# for

for v1 in range(10):
    print(v1)

print()

for v2 in range(1, 11):
    print(v2)

print()

for v3 in range(1, 11, 2):
    print(v3)

print()

# 1 ~ 1000 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print(sum1)
print(sum(range(1, 1001)))
print(sum(range(1, 1001, 4)))
print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Hong']
for name in names:
    print('You are : ', name)

print()

lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print('Current number : ', n)

print()

word = 'Beautiful'
for w in word:
    print('word : ', w)

print()

my_info = {
    "name"  : "Lee",
    "age"   : 33,
    "city"  : "Seoul"
}

for key in my_info:
    print(key, "\t: ", my_info[key])

for val in my_info.values():
    print(val)

print()

name = 'PineApplE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

print()

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)

print()

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print('Current Type : ', type(v))

print()

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 49:
        print("Found : 49!")
        break
else:
    print("Not found : 49")

print()

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

print()

# 변환 예제
name = 'Gentleman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # 순서X