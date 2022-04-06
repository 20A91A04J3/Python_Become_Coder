def fib_seq(n):
    a,b=0,1
    lo=b
    for i in range(3,n+1):
        c=a+b
        if c%2:
            lo=c:
        a=b
        b=c
    return lo


            
   
n=int(input())
res=fib_seq(n)
print(res)
            
    

          
    
     
                                             
