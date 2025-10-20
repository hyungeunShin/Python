# 전역 변수

x = 100
def test1():
    return x * 10
print(test1())

# 함수 내에서 전역 변수를 수정하려면 global 키워드를 사용
y = 100
def test2():
    global y
    y *= 10
    return y
print(test2())