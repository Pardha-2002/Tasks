n=int(input())
for i in range(2,n):
    if n%i==0:
        print('not a palindrome')
        break
else:
    print('palindrome')