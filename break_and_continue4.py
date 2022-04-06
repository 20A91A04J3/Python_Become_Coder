num=int(input())
while num:
    if num%3==0 or num%5==0:
        num-=1
        continue
    print(num,end=' ')
    num-=1
    
