# 병행성

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

temp1 = iter(generator_ex1())

print(next(temp1))
print(next(temp1))
# print(next(temp1))

print()

for v in generator_ex1():
    print(v)

print()


temp2 = [x * 3 for x in generator_ex1()]
print(temp2)

print()

temp3 = (x * 3 for x in generator_ex1())
for i in temp3:
    print(i)

print()

import itertools

gen1 = itertools.count(1, 3)

print(next(gen1))
print(next(gen1))
print(next(gen1))
# ...

print()

gen2 = itertools.takewhile(lambda n : n < 50, itertools.count(1, 3))

for v in gen2:
    print(v)

print()

gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

print()

gen4 = itertools.accumulate([x for x in range(1, 10)])

for v in gen4:
    print(v)

print()

gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print(list(gen5))

print()

gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

print()

gen7 = itertools.product('ABCDE')

print(list(gen7))

print()

gen8 = itertools.product('ABCDE', repeat=2)

print(list(gen8))

print()

gen9 = itertools.groupby('AAABBCCCCDDEEE')

for chr, group in gen9:
    print(chr, ' : ', list(group))