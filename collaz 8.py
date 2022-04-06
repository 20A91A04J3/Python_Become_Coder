def find(n,d):
    c=0
    while n:
        r=n%10
        n=n//10
        if r%d==0 or r%d==1:
            c+=1
        
    return c
     

n,d=map(int,input().split())
res=find(n,d)
print(res)
