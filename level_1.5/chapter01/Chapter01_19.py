# 지역 변수

a = 20
def test():
    global a
    print('3', a)
    a = 35
    return a

print('1', a)

a = 100
print('2', a)
print('4', test())
print('5', a)