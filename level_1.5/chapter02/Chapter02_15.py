# 실행 타임 딜레이

import time

# n = 0
# while n < 5:
#     n += 1
#     time.sleep(1)
#     print(n)

n = 0
while True:
    n += 1
    time.sleep(1)
    print(n)
    if n == 5:
        break