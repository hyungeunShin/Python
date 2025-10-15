# 시퀀스 타입 슬라이싱

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

print(x[4:7])
print(x[-9:-6])
print(x[4:-6])
print(x[-9:7])
print(x[4:7:1])
print(x[-9:-6:1])
print()

print(x[6:3:-1])
print(list(reversed(x[6:3:-1])))