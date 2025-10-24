# 쿠폰 생성

import random

def generate_coupon_code(n):
    characters = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    code_list = []

    random.seed(None)

    for _ in range(0, n):
        choose = random.sample(characters, 6)
        code = ''.join(choose)
        code_list.append(code)
    
    return code_list
        
print(generate_coupon_code(5))