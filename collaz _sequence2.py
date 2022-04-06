n=int(input())
max=n
while True:
    print(n,end=' ')
    if max<n:
        max=n
    if n%2:
        n=n*3+1
    else:
        n=n//2
print(max)
