# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '1111', '2222', sep='-')
print('www', 'naver', 'com', sep='.')
print()

# end 옵션
# end의 default는 \n
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('python study')) # slice
print('{:10.5}'.format('python study'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%f' % (123456.123456789))
print('{:f}'.format(123456.123456789))

print('%06.2f' % (1.123456789))
print('{:06.2f}'.format(1.123456789))