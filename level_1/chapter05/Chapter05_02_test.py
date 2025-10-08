import sys

print(sys.path)

# Chapter06_02.py를 복사해서 C:/math에 붙여넣고 test_module.py로 이름 변경
# 모듈 경로 삽입
# sys.path.append('C:/math')

# print(sys.path)

# import test_module

# print(test_module.add(10, 2))
# print(test_module.sub(10, 2))
# print(test_module.mul(10, 2))
# print(test_module.div(10, 2))
# print(test_module.pow(10, 2))

import Chapter05_02 as test_module

print(test_module.add(10, 2))
print(test_module.sub(10, 2))
print(test_module.mul(10, 2))
print(test_module.div(10, 2))
print(test_module.pow(10, 2))
