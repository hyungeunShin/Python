# 계산

def sum1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum1(10))

def sum2(n):
    return sum(range(n + 1))

print(sum2(10))

def sum3(n):
    return n * (n + 1) // 2

print(sum3(10))
