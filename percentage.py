marks,total=map(int,input().split())
per=marks*100/total
print(per,end=' ')
if per>75:
    print("A+",end=' ')
elif per>60:
    print("A",end=' ')
elif per>50:
    print("B",end=' ')
else:
    print("c",end=' ')
