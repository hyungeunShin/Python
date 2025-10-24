# Dict 조회

d = {'USA': 36, 'Germany': 17, 'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

# def search_dict1(word):
#     try:
#         c = dict((k.lower(), v) for k, v in d.items())
#         return c[word]
#     except:
#         return 'No results were found for your search.'

# print(search_dict1(input('Enter Key: ').lower()))

def search_dict2(word):
    c = dict((k.lower(), v) for k, v in d.items())
    return c.get(word, 'No results were found for your search.')

print(search_dict2(input('Enter Key: ').lower()))