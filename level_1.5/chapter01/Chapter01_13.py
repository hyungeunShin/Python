# Dict 데이터 필터링

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

a = {}
for item in d:
    if d[item] > 25:
        a.update({item: d[item]})
print(a)

b = {}
for k, v in d.items():
    if v > 25:
        b[k] = v
print(b)

print({k: v for k, v in d.items() if v > 25})

print(dict(((k, v) for k, v in d.items() if v > 25)))

# print(list(filter(lambda v: print(v), d.items())))
print(dict(filter(lambda v: v[1] > 25, d.items())))
