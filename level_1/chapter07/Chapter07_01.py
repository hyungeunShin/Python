# built-in function

# 절대값
print(abs(-3))
print()

# any, all: iterable 요소 검사
print(all([1, 2, 3]))
print(all([1, 2, 0]))
print(any([1, 2, 3]))
print(any([1, 2, 0]))
print()

# chr: 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(65))
print(ord('A'))
print()

# enumerate: 인덱스 + Iterable 객체
for index, value in enumerate(['a', 'b', 'c', 'd']):
    print(index, value)

print()

# filter
def conv_pos(x):
    return abs(x) > 2

print(filter(conv_pos, [1, 2, -3, 4, 5, -6]))
print(list(filter(conv_pos, [1, 2, -3, 4, 5, -6])))
print(list(filter(lambda x: abs(x) > 2, [1, 2, -3, 4, 5, -6])))
print()

# id
print(id(5))
print(id(int('5')))
print()

# len
print(len('abcdef'))
print(len([1, 2, 3, 4, 5]))
print()

# max, min
print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('python study'))
print()

# map
def conv_mul(x):
    return x * 2

print(list(map(conv_mul, [1, 2, 3, 4])))
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))
print()

# pow
print(pow(2, 5))
print()

# range
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))
print()

# round
print(round(6.5781, 2))
print(round(5.6))
print()

# sorted
print(sorted([6, 7, 4, 3, 1, 2]))
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))
print()

# sum
print(sum([1, 2, 3, 4]))
print(sum(range(1, 101)))
print()

# type
print(type({}))
print(type(()))
print(type([]))
print()

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20], [40, 50, 60])))
print(list(zip([10, 20, 30], [40, 50, 60]))[2])
print(type(list(zip([10, 20, 30], [40, 50, 60]))[0]))