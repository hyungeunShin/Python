# 문자열

def cnt_word1(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()
    txt = txt.replace(',', ' ')
    txt_list = txt.split(' ')
    return len(txt_list)

print(cnt_word1('./resource/Chapter02_02.txt'))

import re

def cnt_word2(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()
    txt_list = re.split(' |,', txt)
    return len(txt_list)

print(cnt_word2('./resource/Chapter02_02.txt'))