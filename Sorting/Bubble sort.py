n=int(input("Enter number:"))
arr=[]
for _ in range(n):
    m=int(input("Enter an element:"))
    arr.append(m)
for i in range(len(arr)):
    swap=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=True
    if not swap:
        break
print(arr)