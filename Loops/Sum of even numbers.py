numbers=int(input("Enter a number upto which you want sum:"))
sum=0
for num in range(1, numbers+1):
    if num%2==0:
        sum=sum+num
print(sum)
