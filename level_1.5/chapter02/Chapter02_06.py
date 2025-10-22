# 파일 쓰기

import os

filenames = ['A', 'B', 'C', 'D', 'F', 'G']
contents1 = ['Python', 'JavaScript', 'PHP', 'Rust', 'Solidity', 'Assembly']
contents2 = [contents1[:] for _ in range(6)]

def write_contents1(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    
    for n, c in zip(filenames, contents1):
        with open(filepath + n + '.txt', 'w') as file:
            file.write(c)

write_contents1('./resource/Chapter02_06-1/')

def write_contents2(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    
    for n, c in zip(filenames, contents2):
        with open(filepath + n + '.txt', 'w') as file:
            file.writelines(c + '\n' for c in c)

write_contents2('./resource/Chapter02_06-2/')