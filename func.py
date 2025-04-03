def get():
    name=input()
    age=int(input())
    company=input()
    display(name,age,company)
def display(n,a,c):
    print("name:",n)
    print('age:',a)
    print('company:',c)
get()