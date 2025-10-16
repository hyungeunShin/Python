# 중복 제거

x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 'a', 'a', 'b', 'b']

a = []
for i in x:
    if i not in a:
        a.append(i)

print(a)

print(list(set(x)))

from collections import OrderedDict

print(list(OrderedDict.fromkeys(x)))