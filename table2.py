num,r=map(int,input().split())
n=num
d=1
for i in range(n,2*r):
    if i<1:
        print(num,n,num*n)
    else:
        print(num,d,num*d)
        d-=1
    
        


          
