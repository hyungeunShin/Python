# while

n = 5
while n > 0:
    print(n)
    n -= 1

print()

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())

print()

# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')  

print()

# continue
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')   

print()

i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1

print()

# While - else 구문
n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print('else out.')

print()

a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'Not Found in list')
    
    
# 무한반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())