# 비교
# is, is not -> 참조, 객체 비교 
# == , != -> 값 비교
# 값, 참조가 같은 비교는 is 사용

x = 15
y = 15

print(x == y)
print(x is y)
print()

x = ['orange', 'apple']
y = x
print(x == y)
print(x is y)
print(f'c value, id : {x}, {hex(id(x))}')
print(f'd value, id : {y}, {hex(id(y))}')
print()

x = ['orange', 'apple']
y = ['orange', 'apple']
print(x == y)
print(x is y)
print(x, hex(id(x)))
print(y, hex(id(y)))
print()

x = []
y = x
z = x + y

print(x == y)
print(x is y)
print(x == z)
print(x is z)

print(x, hex(id(x)))
print(y, hex(id(y)))
print(z, hex(id(z)))
