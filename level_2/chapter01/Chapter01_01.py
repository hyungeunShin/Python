# 클래스

# 일반적인 코딩

car_company_1 = 'car1'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower': 100},
    {'price': 5000}
]

car_company_1 = 'car2'
car_detail_1 = [
    {'color': 'black'},
    {'horsepower': 200},
    {'price': 6000}
]

# 리스트 구조
# 인덱스 접근 시 실수 가능성

car_company_list = ['car1', 'car2']
car_detail_list = [
    {'color': 'white', 'horsepower': 100, 'price': 5000},
    {'color': 'black', 'horsepower': 200, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 중 문제, 키 조회 예외 처리 등

car_dicts = [
    {'car_company': 'car1', 'car_detail': {'color': 'white', 'horsepower': 100, 'price': 5000}},
    {'car_company': 'car2', 'car_detail': {'color': 'black', 'horsepower': 200, 'price': 6000}},
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
car1 = Car('car1', {'color': 'white', 'horsepower': 100, 'price': 5000})
car2 = Car('car2', {'color': 'black', 'horsepower': 200, 'price': 6000})

print(car1)
print(car2)

print()

print(car1.__dict__)
print(car2.__dict__)

print()

car_list = []

car_list.append(car1)
car_list.append(car2)

print(car_list)

print()

for x in car_list:
    print(x)
    print(repr(x))