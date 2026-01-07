# 클래스 변수, 인스턴스 변수

class Car():
    """
    Car class
    Author: OO
    Date: OOOO.OO.OO
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        # self.car_count = -1
        Car.car_count += 1
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1

car1 = Car('car1', {'color': 'white', 'horsepower': 100, 'price': 5000})
car2 = Car('car2', {'color': 'black', 'horsepower': 200, 'price': 6000})

print(id(car1))
print(id(car2))

print()

print(car1._company == car2._company)
print(car1 is car2)

print()

print(dir(car1))
print(dir(car2))

print()

print(car1.__dict__)
print(car2.__dict__)

print()

print(Car.__doc__)

print()

Car.detail_info(car1)
Car.detail_info(car1)
car1.detail_info()
car2.detail_info()

print()

print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__))

print()

print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

del car2

print(Car.car_count)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))