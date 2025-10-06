# 기본 선언
n = 1
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 1
print(x, y, z)
print()

# 재선언
var = 75
var = "Change Var"
print(var)
print(type(var))
print()

# Object References
print(123)
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# id(identity) 확인
m = 1
n = 2
print(id(m))
print(id(n))
print()

# 같은 오브젝트 참조
a = 1
b = 1
print(id(a))
print(id(b))
print(id(a) == id(b))
print()
