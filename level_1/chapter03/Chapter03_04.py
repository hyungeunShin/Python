# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) ==> 불변

a = ()
b = (1,) # 원소가 하나일 때 뒤에 , 필요
c = (11, 12, 13, 14)
d = (100, 1000, 'A', 'B', 'C')
e = (100, 1000, ('A', 'B', 'C'))

# 인덱싱
print(d[-1])
print(e[-1][1])
print(list(e[-1][1]))
print()

# d[0] = 1500 ==> 'tuple' object does not support item assignment

# 슬라이싱
print(d[0:3])
print(d[2:])
print(e[2][1:3])
print()

# 튜플 연산
print(c + d)
print(c * 3)
print()

# 튜플 함수
a = (5, 2, 3, 1, 4)
print(a.index(3))
print(a.count(3))

# 팩킹
t1 = ('foo', 'bar', 'baz', 'qux')
t2 = 1, 2, 3
t3 = 4, 
print(t1)
print(t2)
print(t3)
print()

# 언팩킹1
(x1, x2, x3, x4) = t1
print(x1, x2, x3, x4)
x1, x2, x3 = t2
print(x1, x2, x3)
x4, x5, x6 = (4, 5, 6)
print(x4, x5, x6)