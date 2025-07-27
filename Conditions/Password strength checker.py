password=str(input("Create password:"))
if len(password)<6:
    print("The password is weak.")

elif 6<=len(password)<=10 :
    print("The strength of your password is medium.")    

else :
    print("The password is strong.")