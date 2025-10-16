# Range, Map, Lambda

a = []
for i in range(1, 16):
    a.append(str(i * 10))

print(a)

print([str(i * 10) for i in range(1, 16)])

print(list(map(lambda i: str(i * 10), range(1, 16))))