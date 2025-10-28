# 파일 읽기 & 쓰기

filepath = './resource/Chapter03_08.txt'
file = open(filepath, 'a+')

while True:
    print('--------------------------')
    print('1. read')
    print('2. write')
    print('3. exit')
    print('--------------------------')

    menu = int(input('Select a menu number: '))

    if menu == 1:
        file = open(filepath, 'r')
        print(file.read())

        print()
        print('--------------------------')
        print('>> Data read complete. <<')
        print('--------------------------')

    elif menu == 2:
        file = open(filepath, 'a+')
        text = input('Write a text\n')
        file.write(text + '\n')

        print()
        print('--------------------------')
        print('>> Data write complete <<')
        print('--------------------------')
    
    elif menu == 3:
        file.close()

        print()
        print('--------------------------')
        print('>> Program exit. <<')
        print('--------------------------')
        break