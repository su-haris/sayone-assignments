l2 = input('Enter numbers separated by commas')
t1 = l2.split(",")
l1 = []
print('Original list:', t1)

y = len(t1)

for i in range(y):
    if int(t1[i]) % 2 == 1:
        l1.append(t1[i])


l1.sort()
print('Smallest Odd no is', l1[0])
