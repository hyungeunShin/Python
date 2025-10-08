# input

# 예제 1
# name = input('Enter Your Name: ')
# grade = input('Enter Your Grade: ')
# company = input('Enter Your Company: ')
# print(name, grade, company)

# 예제 2
# number = input('Enter Number: ')
# name = input('Enter Name: ')
# print(type(number))
# print(type(name))

# 예제3(계산)
# number1 = int(input('Enter number1: '))
# number2 = int(input('Enter number2: '))
# total = number1 + number2
# print(total)

# 예제4
# float_number = float(input('Enter a float number: '))
# print(float_number)

# 예제5
# print('FirstName - {0}, LastName - {1}'.format(input('Enter first name: '), input('Enter second name: ')))

# 예제6
# try:
#     n = int(input('Enter a number: '))
#     print('Your number is', n)
# except ValueError:
#     print('This is not number')

# 예제7
while True:
    try:
        n = int(input('Enter a number: '))
        break
    
    except ValueError:
        print('This is not number. Try again.')
        
print('Your number is', n)