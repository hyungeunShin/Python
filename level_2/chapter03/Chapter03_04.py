# immutable Dict
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# d_frozen['key1'] = 'value2'

print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

print()

# 선언 최적화
from dis import dis

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print()

# Comprehending Set
from unicodedata import name

print({chr(i) for i in range(0, 256)})
print({name(chr(i), '') for i in range(0, 256)})