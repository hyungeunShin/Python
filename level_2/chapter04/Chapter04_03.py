# 클로저

def closure_ex1():
    # Free variable
    series = []

    def average(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return average

avg1 = closure_ex1()
print(avg1(10))
print(avg1(20))
print(avg1(30))

print()

print(dir(avg1))
print()
print(dir(avg1.__code__))
print()
print(avg1.__code__.co_freevars)
print()
print(dir(avg1.__closure__))
print()
print(avg1.__closure__[0].cell_contents)
print()

# 잘못된 클로저
def closure_ex2():
    # Free variable
    total = 0
    cnt = 0

    def average(v):
        total += v
        cnt += 1
        return total / cnt
    
    return average

avg2 = closure_ex2()
# print(avg2(10))

def closure_ex3():
    # Free variable
    total = 0
    cnt = 0

    def average(v):
        nonlocal total, cnt
        total += v
        cnt += 1
        return total / cnt
    
    return average

avg3 = closure_ex3()
print(avg3(10))
print(avg3(20))
print(avg3(30))