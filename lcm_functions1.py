a=int(input())
b=int(input())
big=max(a,b)
small=min(a,b)
a=big
i=1
while True:
    print(big,small)
    if big%small==0:
        print(big)
        break
    else:
        big=a*i
        i+=1
