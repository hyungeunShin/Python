chars = '+_)(*&^%$#@!~)'

# Non Comprehending Lists
code_list1 = []

for s in chars:
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list3)
print(code_list4)

print()

# Generator
import array

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g)
print(array_g.tolist())

print()

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)

print()

# 주의점
marks1 = [['~'] * 3 for _ in range(3)]
marks2 = [['~'] * 3] * 3

print(marks1)
print(marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

print()

print([id(i) for i in marks1])
print([id(i) for i in marks2])