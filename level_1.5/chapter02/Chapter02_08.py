# 사용자 입력

x = int(input('Enter first value\t: '))
y = int(input('Enter second value\t: '))
z = int(input('Enter third value\t: '))
print((x + y + z) / 3)

x, y, z = input('Enter three values: ').split()
print((int(x) + int(y) + int(z)) / 3)

l = list(map(int, input('Enter three values: ').split()))
print(sum(l) / len(l))