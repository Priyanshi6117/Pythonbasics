distance=int(input("Enter how much distance you have to travel:"))
if distance<3:
    print("It's preferable for you to walk.")
elif 3<distance<15:
    print("It's preferable for you to ride a bike.")
else :
    print("It's preferable for you to take a car.")