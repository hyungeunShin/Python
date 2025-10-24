# Dict 반복문

l = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

d1 = dict(enumerate(l))
print(d1)

d2 = dict(enumerate(l, start=100))
print(d2)