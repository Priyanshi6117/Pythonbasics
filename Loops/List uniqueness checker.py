list=input("Enter elements separated by space:").split()
print(list)
unique=set()
for item in list:
    if item in unique:
        print("Duplicate:",item)
        break
    unique.add(item)
 