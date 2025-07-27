pet=input("Which pet do you own?:")
age=int(input("What is your pet's age?:"))
if (pet=="dog" and age<2):
    print("It is recommended that you give your pet puppy food.")
elif (pet=="cat" and age>5):
    print("It is recommended that you give your pet senior cat food.")
else:
    print("False.")