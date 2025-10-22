# 문자열 포맷

x = 10
y = 20
s = 308276567
n = 'Kim'

print('n = %s, s = %d, sum=%d' % (n, s, (x + y)))
print()

print('n = {n}, s = {s}, sum={sum}'.format(n = n, s = s, sum = x + y))
print()

print(f'n = {n}, s = {s}, sum={x + y}')
print()

from string import Template
t = Template('n = $n, s = $s, sum=$sum')
print(t.substitute(n = n, s = s, sum = x + y))
print()

# 2진수: b, 8진수: o, 16진수: x|X
k = 77
print(f'2진수: {k:b}, 8진수: {k:o}')
print(f'16진수: {k:x}, {k:X}')
print()

# 구분기호
m = 10000000000
print(f'{m:,}')
print()

# 정렬
g = 20
print(f'{g:10}')
print(f'{g:^10}')
print(f'{g:<10}')
print(f'{g:>10}')
print()

# 채우기
print(f'{g:-^10}')
print(f'{g:*^10}')