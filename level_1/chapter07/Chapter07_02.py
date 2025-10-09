# external function

# sys: 실행 관련 제어
import sys

print(sys.argv)
# sys.exit()
# print('1')
print(sys.path)
print()

# pickle: 객체 파일 읽기, 쓰기
import pickle

# 쓰기
f = open("test.obj", 'wb')
obj = {1: 'A', 2: 'B', 3: 'C'}
pickle.dump(obj, f)
f.close()

# 읽기
f = open("test.obj", 'rb')
data = pickle.load(f)
print(data)
f.close()
print()

# os: 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
import os

print(os.environ)
print(os.environ['USERNAME'])
print(os.getcwd())
print()

# time: 시간 관련 처리
import time

print(time.time())
print(time.localtime(time.time()))
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# for i in range(5):
#     print(i)
#     time.sleep(1)

print()

# random
import random

print(random.random()) # 0 ~ 1 실수
print(random.randint(1, 45))
print(random.randrange(1, 46))

d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

c = random.choice(d)
print(c)
print()

# webbrowser : 본인 OS 의 웹 브라우저 실행
import webbrowser

webbrowser.open("www.google.com")
webbrowser.open_new("www.google.com")