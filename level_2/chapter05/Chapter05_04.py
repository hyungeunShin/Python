# futures

import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]

def sum_generator(n):
    return sum(a for a in range(1, n + 1))

def main():
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    with futures.ThreadPoolExecutor(max_workers=worker) as executor:
        result = executor.map(sum_generator, WORK_LIST)

    end_time = time.time()

    msg = '\nResult -> {} Time : {:.2f}s'
    print(msg.format(list(result), (end_time - start_time)))

if __name__ == '__main__':
    main()