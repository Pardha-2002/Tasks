import re
password_pattern=r'[a-zA-Z0-9!@#$%*]{6,}'
str='Password@123'
match=re.search(password_pattern,str)
if match:
    print("valid password")
else:
    print('not valid')