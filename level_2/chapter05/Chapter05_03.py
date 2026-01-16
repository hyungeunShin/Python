# Coroutine

def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))

cr1 = coroutine1()

print(cr1)

# next(cr1)

# cr1.send(10)

print()

# cr2 = coroutine1()
# cr2.send(100)

# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

# print(next(cr3))
# cr3.send(100)
# cr3.send(500)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

cr3.send(100)

print()

def coroutine3():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

cr4 = coroutine3()

print(next(cr4))
print(next(cr4))
print(next(cr4))
print(next(cr4))
print(next(cr4))

cr5 = coroutine3()

print(list(cr5))

print()

def coroutine4():
    yield from 'AB'
    yield from range(1, 4)

cr6 = coroutine4()

print(next(cr6))
print(next(cr6))
print(next(cr6))
print(next(cr6))
print(next(cr6))