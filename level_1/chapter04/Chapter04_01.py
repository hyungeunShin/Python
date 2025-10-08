# fucntion

# 예제 1
def first_func(w):
    print("Hello, ", w, sep='')

first_func("Gentleman")
print()

# 예제 2
def return_func(w):
    return "Hello, " + str(w)

print(return_func("Gentleman"))
print()

# 예제 3
def func_mul1(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul1(10)
print(x, y, z)
print()

# 예제 4
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

t = func_mul2(20)
print(t)
print()

# 예제 5
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

l = func_mul3(30)
print(l)
print()

# 예제 6
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul4(40)
print(d)
print()

# *args, **kwargs

# *args(언팩킹) - 튜플 형식
def args_func(*args):
    for i, v in enumerate(args):
        print('Reuslt : {}'.format(i), v)

args_func('Lee', 'Kim', 'Park')
print()

# **kwargs(언팩킹) - 딕셔너리 형식
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v], sep=': ')

kwargs_func(name1='Lee', name2='Park', name3='Kim', age=12)
print()

# 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    print(type(args))
    print(type(kwargs))

example(10, 20, 'Lee', 'Kim', 'Park', age1=10, age2=20, age3=30)
print()

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In Func')
    func_in_func(num + 100)

nested_func(100)
# func_in_func(100)
print()

# 람다
def mul_func(x, y):
    return x * y

lambda_mul_func = lambda x, y: x * y

print(mul_func(1, 5))
print(lambda_mul_func(1, 5))
print()

def func_final(x, y, func):
    print(x * y * func(10, 10))

func_final(1, 2, mul_func)
func_final(1, 2, lambda_mul_func)
func_final(1, 2, lambda x, y: x * y)
print()

# 힌트
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print(tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("gentleman", 10)