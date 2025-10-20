# 함수 인자

# Non-default argument follows default argument
# def greet(msg='Good morning!', name):
#     return 'Hi! ' + name + ', ' + msg

def greet(name, msg='Good morning!'):
    return 'Hi! ' + name + ', ' + msg

print(greet('Kim'))
print(greet('Park', 'How do you do?'))
print()

def add1(a, b=10, c=15):
    print(a, b, c)
    return a + b + c

print(add1(15))
print(add1(b=100, c=25, a=30))
print()

def add2(*d):
    total = 0
    for i in d:
        total += i
    return total

print(add2(1, 2, 3, 4))
print(add2(*(i for i in range(1, 11))))
print()

print(range(1, 11))
print(i for i in range(1, 11))
print(*(i for i in range(1, 11)))