# 비밀번호 체크

while True:
    result = []
    pw = input('Enter Password: ')
    print()

    if not any(i.isdigit() for i in pw):
        result.append('최소 1개 이상의 숫자가 포함되야 합니다.')
    if not any(i.isupper() for i in pw):
        result.append('최소 1개 이상의 대문자가 포함되야 합니다.')
    if len(pw) < 8:
        result.append('패스워드는 8자 이상 입력해 주세요.')

    if len(result) == 0:
        print('O')
        break
    else:
        for txt in result:
            print('-', txt)