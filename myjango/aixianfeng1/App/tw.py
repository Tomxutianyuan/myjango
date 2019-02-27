# _*_coding:utf-8_*_
def move(n,a,b,c):
    if n==1:
        print(a,"move to ",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')