import re

regexp = '91?[0-9]{10}$'
mob = input('Enter number beginning with 91 (eg: 91xxxxxxxxxx)')

if re.search(regexp, mob):
    print('Valid mobile')

else:
    print('Invalid mobile')
