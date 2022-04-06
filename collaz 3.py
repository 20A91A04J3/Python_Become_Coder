def find_max(n,target):
    while True:
        if n==target:
            return True
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
def seq_count(n):
    c=0
    while True:
        c+=1
        if n==1:
            return c
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
def seq(n,m):
    c=0
    while True:
        c+=1
        print(n,end=' ')
        if n==1 or m==c:
            return
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
n,m=map(int,input().split())
res=seq_countn)
print(res)



        
            
