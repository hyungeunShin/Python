# 시퀀스 타입 인덱싱

x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']

print(x.index('Banana'))
print(x[4])
print('Banana' in x)
print(x[x.index('Banana')])
print(x[x.index('Banana', 0, len(x))])