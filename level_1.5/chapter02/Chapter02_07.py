# 멀티 파일 읽기

import os

def read_text_file1(filepath):
    outputs = []

    for file in os.listdir(filepath):
        # print(file)
        if file.endswith('.txt'):
            target_path = f'{filepath}/{file}'
            
            with open(target_path, 'r') as f:
                outputs.append(f.read())
    
    return outputs

print(read_text_file1('./resource/Chapter02_07'))

import glob

def read_text_file2(filepath):
    outputs = []

    for file in glob.glob(filepath + '/*.txt'):
        with open(file, 'r') as f:
            outputs.append(f.read())

    return outputs

print(read_text_file2('./resource/Chapter02_07'))