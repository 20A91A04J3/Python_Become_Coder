n=int(input())
ec=0
oc=0
while True:
    print(n,end=' ')
    if n==1:
        break
    if n%2:
        oc+=n
        n=n*3+1
    else:
        ec+=n
        n=n//2
print()
print(ec,oc+1)
