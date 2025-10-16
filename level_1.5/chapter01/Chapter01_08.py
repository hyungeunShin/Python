# Range

a = []
for i in range(1, 21):
    if i % 2 == 0:
        a.append(i)
    else:
        a.append(i * 10)

print(a)

# List Comprehension

print([x if x % 2 == 0 else x * 10 for x in range(1, 21)])