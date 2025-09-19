arr=[0,2,4,5,6,9,10]
tar=4
start=0
end=len(arr)-1
found=False
while start<=end:
    mid=(start+end)//2
    if (arr[mid]>tar):
        end=mid-1
    elif (arr[mid]<tar):
        start=mid+1
    else:
        print(mid)
        found=True
        break
if not found:
    print("-1")
