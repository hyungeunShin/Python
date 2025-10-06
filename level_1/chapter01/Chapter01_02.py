# 파이썬 3가지 format
x = 50
y = 100
z = 308276567
text = 'Lee'

# 출력 1
ex1 = 'z = %s, text = %s, sum = %d' % (z, text, (x + y))
print(ex1)

# 출력 2
ex2 = 'z = {z}, text = {text}, sum = {sum}'.format(z = z, text = text, sum = x + y)
print(ex2)

# 출력 3
ex3 = f'z = {z}, text = {text}, sum = {x + y}'
print(ex3)

# 구분기호
m = 100000000
print(f'm : {m:,}')
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t = 20
print(f't : {t:10}')
print(f't : {t:^10}')
print(f't : {t:<10}')
print(f't : {t:>10}')
print()

print(f't : {t:-^10}')
print(f't : {t:#<10}')