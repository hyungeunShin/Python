# 병렬 처리

a = ['one', 'two', 'three', 'four']
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

r = {}
for x, y, z in zip(a, b, c):
    r[x] = y * z
print(r)

print({x: y * z for x, y, z in zip(a, b, c)})

print(dict((x, y * z) for x, y, z in zip(a, b, c)))