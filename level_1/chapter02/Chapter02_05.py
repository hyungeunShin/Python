# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)
# 범용적으로 가장 많이 사용

# 선언
a = {'name': 'Kim', 'phone': '010-1111-2222', 'birth': '000101'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'name'  : 'Gentleman',
    'city'  : 'Seoul',
    'age'   : 20,
    'grade' : 'A',
    'status': True
}
e = dict([
    ('name'  , 'Gentleman'),
    ('city'  , 'Seoul'),
    ('age'   , 20),
    ('grade' , 'A'),
    ('status', True)
])
f = dict(
    name   = 'Gentleman',
    city   = 'Seoul',
    age    = 20,
    grade  = 'A',
    status = True
)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print()

# 출력
print(a['name']) # 존재X -> 에러 발생
print(a.get('name')) # 존재X -> None 처리
print(b[0])
print(b.get(0))
print(c['arr'])
print(c['arr'][3])
print(c.get('arr'))
print(d.get('age'))
print()

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
print(a)
print()

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__) 사용 가능
print(a.keys())
print(b.keys())
print(c.keys())
print(list(d.keys()))
print(list(e.keys()))
print()

print(a.values())
print(b.values())
print(c.values())
print(list(d.values()))
print(list(e.values()))
print()

print(a.items())
print(b.items())
print(c.items())
print(list(d.items()))
print(list(e.items()))
print()

print(a.pop('name'))
print(a)
print(c.pop('arr'))
print(c)
print()

print(f.popitem())
print(f.popitem())
print(f.popitem())
print(f.popitem())
print(f.popitem())
print(f)
print()

print('name' in d)
print('address' in d)
print()

# 수정
a['phone'] = '010-5555-6666'
print(a)

a.update(birth='250101')
print(a)
temp = {'address': 'Busan'}
a.update(temp)
print(a)