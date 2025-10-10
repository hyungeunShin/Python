# csv

import csv

# 예제 1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    # next(reader) # header skip
    # for c in reader:
    #     print(c)
    #     print(' : '.join(c))

print()

# 예제 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    # for c in reader:
    #     print(c)

print()

# 예제 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    # for c in reader:
    #     print(c)
    #     for k, v in c.items():
    #         print(k, v)
    #     print('-' * 8)

print()

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8', newline='') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

# 예제5
with open('./resource/write2.csv', 'w', newline='') as f:
    fields = ['one', 'two', 'three']
    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()

    for v in w:
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})