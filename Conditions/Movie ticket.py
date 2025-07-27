Day=str(input("Enter day:"))
age=int(input("Enter your age:"))
if age<18 :   
    price=8
    print("You are a child and your ticket price is $",price)
else :
    price=12
    print("You are an adult and your ticket price is $",price)

if Day=="wednesday" :
    price-=2
    print("But you got a $2 discount and your ticket costs $",price)