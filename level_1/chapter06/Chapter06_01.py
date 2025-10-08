# exception

# SyntaxError
# print('error)
# print('error'))
# if True
#     pass

# NameError
# print(a)

# ZeroDivisionError
# print(5 / 0)

# IndexError
x = []
# print(x[1])
# x.pop()

# KeyError
dic = {}
# print(dic['a'])

# AttributeError
import time
# print(time.time2())

# ValueError
# x.remove(1)

# FileNotFoundError
# f = open('test.txt')

# TypeError
# print(1 + "1")

name = ['Kim', 'Lee', 'Park']

# 예제 1
# try:
#     name.index('Kim')
# except ValueError:
#     print('ValueError')
# else:
#     print('else')

# 예제 2
# try:
#     name.index('Kim')
# except Exception:
#     print('Error')
# else:
#     print('else')

# 예제 3
# try:
#     name.index('Kim1')
# except Exception as e:
#     print(e)
# else:
#     print('else')
# finally:
#     print('finally')

# 예제 4
try:
    if(2 > 1):
        raise ValueError('ValueError')
except Exception as e:
    print(e)
else:
    print('else')
finally:
    print('finally')