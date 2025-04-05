import re
url_pattern=r'^http?://+[a-zA-Z0-9.]+\.[a-zA-Z]{2,}'
str='http://app.revature.com/'
z=re.search(url_pattern,str)
if z:
    print('match found')
else:
    print('not')