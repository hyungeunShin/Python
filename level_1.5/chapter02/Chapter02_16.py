# 실행 타임 딜레이

import time

# for i in [.5, 1, 1.5, 2, 2.5, 3]:
#     time.sleep(i)
#     print(f'Delayed for {i} seconds')

# n = .5
# while True:
#     time.sleep(n)
#     print(f'Delayed for {n} seconds')
#     n += .5

#     if n > 3:
#         break

def sleep_out(n):
    time.sleep(n)
    print(f'Delayed for {n} seconds')

for i in [.5, 1, 1.5, 2, 2.5, 3]:
    sleep_out(i)