# 파일 필터링

def read_text_file1(filepath):
    result = 0

    with open(filepath, 'r') as f:
        for line in f.readlines():
            country, value = line.strip().split(',')
            
            if country.lower().startswith('c'):
                result += int(value)

    return result

print(read_text_file1('./resource/Chapter03_05.txt'))

import csv

def read_text_file2(filepath):
    result = 0

    with open(filepath, 'r') as f:
        for row in csv.reader(f, delimiter=','):
            if row[0].lower().startswith('c'):
                result += int(row[1])

    return result

print(read_text_file2('./resource/Chapter03_05.txt'))