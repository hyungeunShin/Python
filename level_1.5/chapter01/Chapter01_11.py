# Dict 합

d = {'a': 17, 'b': 114, 'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

total = 0
for i in d.values():
    total += i
print(total)

print(sum(d.values()))

# for item in d:
#     print(item)

print(sum([d[item] for item in d]))

from functools import reduce
print(reduce(lambda x, y: x + y, d.values(), 0))