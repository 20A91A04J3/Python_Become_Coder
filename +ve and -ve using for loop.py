num,r=map(int,input().split())
es=0
os=0
for i in range(1,r+1):
    v=num*i
    if v%2==0:
        es+=v
    else:

        os+=v
print(es,os)
