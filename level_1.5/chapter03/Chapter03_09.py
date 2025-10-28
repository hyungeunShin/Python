# 폰북

member = {
    0: {'Name': 'A', 'Phone': '1'},
    1: {'Name': 'B', 'Phone': '2'},
}

def list_member(d):
    for pid in d:
        print('\nPID:', pid + 1)
        for p_info in d[pid]:
            print(p_info, ':', d[pid][p_info])

def add_member(d):
    name = input('Name\t: ')
    phone = input('Phone\t: ')

    name_check = False

    for pid in d:
        if name == d[pid].get('Name'):
            name_check = True

    if name_check is True:
        print('\n이미 존재하는 회원')
    else:
        d[len(d)] = {'Name': name, 'Phone': phone}
        print('\n추가 완료')
    
    return d

def delete_member(d):
    name = input('name\t: ')

    for pid in d:
        if name == d[pid].get('Name'):
            del d[pid]
            print('\n삭제완료')
            return d
        
    print('\n존재하지 않는 회원')

def mainmenu():
    while True:
        menu = input('''
----MAIN MENU----
1: 리스트
2: 추가
3: 삭제
4: 종료
선택: ''')

        if menu == '1':
            list_member(member)
        elif menu == '2':
            add_member(member)
        elif menu == '3':
            delete_member(member)
        elif menu == '4':
            return False
        else:
            print('\n없는 메뉴')

mainmenu()