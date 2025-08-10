n=5
for i in range(n):
    p=5
    for j in range(i):
        print(' ',end=' ')
        p-=1
    for j in range(i,n):
        print(p,end=' ')
        p-=1
    print()