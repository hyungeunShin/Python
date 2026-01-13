# 일급 함수

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

class A:
    pass

print(factorial(5))
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(5))
print(list(map(var_func, range(1, 6))))

print()

# 고위 함수
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()

# reduce()
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

print()

# 익명 함수
print(reduce(lambda x, t: x + t, range(1, 11)))

print()

# callable: 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))

print()

# partial: 인수 고정
from functools import partial
from operator import mul

five = partial(mul, 5)
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))