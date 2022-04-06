def even_odd(n):
    ec=0
    os=0
    while n:
        d=n%10
        n=n//10
        if d%2==0:
            ec+=1
        else:
            os+=1
    print(ec,os)
n=int(input())
even_odd(n)

