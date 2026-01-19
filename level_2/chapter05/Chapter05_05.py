# futures

import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

WORK_LIST = [10000, 100000, 1000000, 10000000]

def sum_generator(n):
    return sum(a for a in range(1, n + 1))

def main1():
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    future_list = []
    with ThreadPoolExecutor(max_workers=worker) as executor:
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            future_list.append(future)
            print('Scheduled for {} : {}'.format(work, future))
        
        result = wait(future_list, timeout=7)

        print('completed task: {}'.format(result.done))
        print('not completed task: {}'.format(result.not_done))
        print([future.result() for future in result.done])

    end_time = time.time()

    msg = '\nTime : {:.2f}s'
    print(msg.format((end_time - start_time)))

def main2():
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    future_list = []
    with ThreadPoolExecutor(max_workers=worker) as executor:
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            future_list.append(future)
            print('Scheduled for {} : {}'.format(work, future))
        
        for future in as_completed(future_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    end_time = time.time()

    msg = '\nTime : {:.2f}s'
    print(msg.format((end_time - start_time)))

if __name__ == '__main__':
    main1()
    print()
    print()
    main2()