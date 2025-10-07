# if

print(type(True))
print(type(False))
print()

if True:
    print("Good")

if False:
    print("Bad")

print()

# 관계연산자
x = 15
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print()

# 참 : "values", [values], (values), {values}, 1
# 거짓 : "", [], (), {}, 0, None
city = ""
if city:
    print("You are in: ", city)
else:
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in: ", city)
else:
    print("Please enter your city")

print()

# 논리연산자
a = 75
b = 40
c = 10
print(a > b and b > c)
print(a > b or b > c)
print(not a > b)
print(not b > c)
print(not True)
print(not False)
print()

# 산술 > 관계 > 논리 순서
print(3 + 12 > 7 + 3)
print(5 + 10 * 3 > 7 + 3 * 20)
print(5 + 10 > 3 and 7 + 3 == 10)
print(5 + 10 > 0 and not 7 + 3 == 10)
print()

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("Pass")
else:
    print("Fail")

print()

id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin":
    print("관리자")

if id2 == "admin" and grade == "platinum":
    print("최상위 관리자")

print()

# 다중 조건문
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

print()

# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print("장학금 100%")
    elif total >= 80:
        print("장학금 80%")
    else:
        print("장학금 70%")
else:
    print("장학금 50%")

print()

# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색
