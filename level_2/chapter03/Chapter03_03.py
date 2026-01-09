t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))

print()

source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

dict1 = {}
dict2 = {}

# no use setdefault
for k, v in source:
    if k in dict1:
        dict1[k].append(v)
    else:
        dict1[k] = [v]

print(dict1)

# use setdefault
for k, v in source:
    dict2.setdefault(k, []).append(v)

print(dict2)

dict3 = {k : v for k , v in source}
print(dict3)