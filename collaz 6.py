n=int(input())
es=0
os=0
while n:
    d=n%10
    n=n//10
    if d%2==0:
        es+=1
    else:
        os+=1
print(es,os+1)
        
        
    
