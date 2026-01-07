# Class Method, Instance Method, Static Method

class Car(object):
    """
    Car class
    Author: OO
    Date: OOOO.OO.OO
    """

    # Class Variable
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'price increased.'

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not Bmw.'
      
car1 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

print()

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.2

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# Bmw 여부(스태틱 메소드 미사용)
def is_bmw(inst):
    if inst._company == 'Bmw':
        return 'OK! This car is {}.'.format(inst._company)
    return 'Sorry. This car is not Bmw.'

# 별도의 메소드 작성 후 호출
print(is_bmw(car1))
print(is_bmw(car2))

print()

# Bmw 여부(스태틱 메소드 사용)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

print()

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
