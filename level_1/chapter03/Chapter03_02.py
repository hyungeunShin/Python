str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()
print(len(str1_t1), len(str2_t2))
print()

# 이스케이프
print("I'm good")
print('I\'m good')
print("Do you have a \"retro games\"?")
print('What\'s on TV?')
print()

# Raw String
raw_s1 = r'C:\Python\test'
raw_s2 = r"\\x\y\z\q"
print(raw_s1)
print(raw_s2)
print()

# 멀티 라인
multi_str1 = """
000000000
111111111
222222222
"""
multi_str2 = \
"""
000000000
111111111
222222222
"""
multi_str3 = '''
AAAAAAAAA
BBBBBBBBB
CCCCCCCCC
'''
print(multi_str1)
print(multi_str2)
print(multi_str3)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "apple"
str_o3 = "Seoul Daejeon Busan Incheon"
str_04 = "bacfde"
print(str_o1 * 3)
print('y' in str_o1)
print('z' in str_o1)
print('p' in str_o1)
print('P' in str_o2)
print()

# 문자열 함수
print("Capitalize: ", str_o2.capitalize()) # 앞 글자 대문자
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('thon', ' Good'))
print("split: ", str_o3.split(' '))
print("sorted: ", sorted(str_04))
print("reversed1: ", reversed(str_o2))
print("reversed2: ", list(reversed(str_o2)))

# 반복
im_str = "Good Job!"
print(dir(im_str))

for i in im_str:
    print(i)
print()

# 슬라이싱
str_sl = 'Nice Python'
print(str_sl[0:3])
print(str_sl[5:11])
print(str_sl[5:])
print(str_sl[:])
print(str_sl[:len(str_sl)])
print(str_sl[1:10:2])
print()
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
print()

# 아스키코드
a = 'z'
print(ord(a))
print(chr(122))