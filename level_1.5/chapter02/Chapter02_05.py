# 리스트 스플릿

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def split_n_list(split_size=3):
    split_list = list()

    for i in range(0, len(a), split_size):
        split_list.append(a[i:i+split_size])
    
    return split_list

print(split_n_list())

split_size = 5
print([a[i:i+split_size] for i in range(0, len(a), split_size)])