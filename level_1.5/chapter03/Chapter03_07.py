# 폴더 재귀 조회

import os

txt_list = []
py_list = []

for root, dirnames, filenames in os.walk('./resource/Chapter03_07'):
    # print(root)
    # print(dirnames)
    # print(filenames)

    for f in filenames:
        ext = f.split('.')[-1]

        if ext == 'txt':
            txt_list.append(f)
        if ext == 'py':
            py_list.append(f)

print(txt_list)
print(py_list)
print()

import glob

print(glob.glob('./resource/Chapter03_07/**/*.txt', recursive=True))
print(glob.glob('./resource/Chapter03_07/**/*.py', recursive=True))