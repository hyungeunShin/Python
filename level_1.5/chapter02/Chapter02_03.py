# 알파벳 쓰기

def write_alphabet1(filepath):
    with open(filepath, 'w') as file:
        for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            file.write(l + ' ')

write_alphabet1('./resource/Chapter02_03-1.txt')

import string

# https://docs.python.org/3/library/string.html
def write_alphabet2(filepath):
    with open(filepath, 'w') as file:
        for l in string.ascii_uppercase:
            file.write(l + '\n')
write_alphabet2('./resource/Chapter02_03-2.txt')