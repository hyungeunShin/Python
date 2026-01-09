print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)

print()

t = (15, 20, 25)
l = [15, 20, 25]

print(id(t))
print(id(l))

t = t * 2
l = l * 2

print(id(t))
print(id(l))

t *= 2
l *= 2

print(id(t))
print(id(l))

print()

# sorted: 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'graph', 'strawberry']
print(sorted(f_list))
print(sorted(f_list, reverse=True))
print(sorted(f_list, key=len))
print(sorted(f_list, key=lambda x: x[-1]))

print(f_list)

print()

# sort: 정렬 후 객체 변경
print(f_list.sort(), f_list)
print(f_list.sort(reverse=True), f_list)
print(f_list.sort(key=len), f_list)
print(f_list.sort(key=lambda x: x[-1]), f_list)