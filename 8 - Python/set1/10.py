s = 0


l2 = input('Enter names separated by commas')
l1 = l2.split(",")

s = len(l1)

print(l1)

if s == 1 and l1[0] == '':
    print('Nobody likes this')

elif s == 1:
    print(l1[0], 'likes this')

elif s == 2:
    print(l1[0], 'and', l1[1], 'likes this')

else:
    print(l1[0], l1[1], 'and', s - 2, 'others likes this')
