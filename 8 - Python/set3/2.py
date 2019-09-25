import re

regexp = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
mail = input('Enter email')

if re.search(regexp, mail):
    print('Valid email')

else:
    print('Invalid email')