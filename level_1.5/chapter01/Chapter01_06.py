# 시퀀스 타입 조회

x = ['grapes', 'mango', 'orange', 'peach', 'apple', 'lime', 'banana', 'cherry', 'tomato', 'kiwi', 'blueberry', 'watermelon']

a = []
for i in range(len(x)):
    if x[i] == 'apple' or x[i] == 'kiwi':
        a.append(x[i].upper())

print(a)

print(list(map(lambda s: s.upper(), filter(lambda f: f == 'apple' or f == 'kiwi', x))))
print([f.upper() for f in x if f == 'apple' or f == 'kiwi'])
