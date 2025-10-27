# 파일 확장자 체크

import os

ext_count1 = {}
for f in os.listdir('./resource/Chapter03_06'):
    ext = f.split('.')[-1]
    ext_count1[ext] = ext_count1.get(ext, 0) + 1
    
print(ext_count1)

ext_count2 = {}
for f in os.listdir('./resource/Chapter03_06'):
    ext = os.path.splitext(f)[1].replace('.', '')
    ext_count2[ext] = ext_count2.get(ext, 0) + 1

print(ext_count2)

import glob

print(glob.glob('./resource/Chapter03_06/*.txt'))
print(glob.glob('./resource/Chapter03_06/*.py'))
