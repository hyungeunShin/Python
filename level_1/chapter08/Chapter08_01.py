# file
# r(read): 읽기 모드, w(write): 쓰기 모드, a(append): 추가 모드, t: 텍스트 모드, b: 바이너리 모드

# 읽기
# 예제 1
f = open('./resource/it_news.txt', 'rt', encoding='UTF-8') # t는 기본 값
# print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
print(f.read())
f.close()

# 예제 2
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    print(f.read())

# 예제 3
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    print(f.read(20))
    print(f.read(20))
    print(f.read(20))
    f.seek(0, 0)
    print(f.read(20))

print()

# 예제 4
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    print(f.readline())
    print(f.readline())

print()

# 예제 5
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()

    for c in cts:
        print(c, end='')

# 쓰기
# 예제 6
with open('./resource/test1.txt', 'wt') as f:
    f.write('I love python1\n')

# 예제 7
with open('./resource/test1.txt', 'at') as f:
    f.write('I love python2\n')

# 예제8
with open('./resource/test2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제 9
with open('./resource/test3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)