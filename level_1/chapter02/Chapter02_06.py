# 집합(Sets) 자료형(순서X, 중복X)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 2, 'A', 'B', 'C'])
d = {'foo', 'bar', 'baz', 'foo', 'qux'}
e = {42, 'foo', (1, 2, 3), 3.14159}

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print()

# 튜플 변환
t = tuple(b)
print(type(t), t)
print(t[0], t[1:3])
print()

# 리스트 변환
l1 = list(c)
l2 = list(e)
print(type(l1), l1)
print(type(l2), l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))
print()

# 합집합
print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))
print()

# 차집합
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))
print()

# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2))
print()

# 부분 집합 확인
s3 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.issubset(s3), s2.issubset(s3))
print(s3.issuperset(s1), s3.issuperset(s2))
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)

s1.remove(2)
print(s1)
# s1.remove(7) => # 존재X -> 에러 발생

s1.discard(3)
print(s1)
s1.discard(7) # # 존재X -> 에러 발생X

# 모두 제거
s1.clear()
print(s1)