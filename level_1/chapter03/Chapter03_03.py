a = []
b = list()
c = [70, 75, 80, 85]
d = [10, 10.0, 'A', 'B', False]
e = [10, 100, ['A', 'B', 'C']]

print(type(a))
print(len(b))
print(d)
print(e, len(e))
print()

# 인덱싱
print(d[1])
print(d[-2])
print(e[-1][1])
print(list(e[-1][1]))
print()

# 슬라이싱
print(d[0:3])
print(d[2:])
print(e[-1][1:3])
print()

# 리스트 연산
print(c + d)
print(c * 3)
#print('Test' + c[0])
print('Test' + str(c[0]))
print()

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

c[0] = 1
print(c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1] = ['a', 'b', 'c']
print(c)
c[1:3] = []
print(c)
del c[2]
print(c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
a.append(6)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3), a[3])
a.insert(2, 7)
print(a)