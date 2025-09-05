n=int(input())
i=int(n/2)
while i<=(n):
    spaces=" "
    stars= "*"*i
    print(spaces*(n-2-i)+stars+" "*(n-1)+stars)
    i+=2
if i==n:
    print("*"*(2*n))
for j in range (0,n):
    print(" "*j,end=' ')
    print("*"*((2*n-1)-(2*j)))
    