# json -> Dict

import json

d = '''
    {
        "group1": [
            {
                "name": "Park",
                "age": "32",
                "sex": "Male"
            },
            {
                "name": "Cho",
                "age": "44",
                "sex": "Female"
            },
            {
                "name": "Kang",
                "age": "39",
                "sex": "Female",
                "married": "No"
            }
        ],
        "group2": [
            {
                "name": "Kim",
                "age": "23",
                "sex": "Male",
                "married": "Yes"
            },
            {
                "name": "Lee",
                "age": "37",
                "sex": "Male",
                "married": "No"
            }
        ],
        "type": {
            "a": "employee",
            "b": "officer",
            "c": "director",
            "d": "manager",
            "e": "service provider"
        }
    }
'''

result1 = json.loads(d)
print(result1)

print()

with open('./resource/Chapter02_13.json', 'r') as file:
    result2 = json.load(file)
    print(result2)