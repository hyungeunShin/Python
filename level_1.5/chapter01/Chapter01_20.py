# 지역 & 전역 변수

def test(x, y):
    global a
    a = 49
    x, y = y, x
    b = 53
    b = 7
    a = 135
    print(a, b, x, y, sep='\t')

a, b, x, y = 8, 13, 33, 44 

test(23, 7)

print(a, b, x, y, sep='\t')
