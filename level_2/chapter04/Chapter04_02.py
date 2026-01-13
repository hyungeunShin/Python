# 클로저
# 함수 안에서 정의된 내부 함수가 외부 함수의 지역 변수를 참조하고 기억하는 기능

def func_v1(a):
    print(a)
    print(b)

# func_v1(10)

b = 20
def func_v2(a):
    print(a)
    print(b)

func_v2(10)

print()

c = 30
def func_v3():
    global c
    print(c)
    c = 40
    print(c)

print(c)
func_v3()
print(c)

print()

class Average():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
    
average = Average()
print(average(10))
print(average(20))
print(average(30))