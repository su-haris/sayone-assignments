t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
l1 = []
print('Original tuple:', t1)

y = len(t1)

for i in range(y):
    if t1[i] % 2 == 0:
        l1.append(t1[i])


print('New Tuple:', tuple(l1))
