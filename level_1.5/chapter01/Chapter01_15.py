# Dict 반복문

d = dict(one = list(range(1, 11)), two = list(range(11, 21)), three = list(range(21, 31)))

for k, v in d.items():
    print(f'{k}\t: {v}')