coffee=input("Which size would you like to have?(Small,Medium,Large):")
espresso_shot=input("Would you like to have an extra shot of espresso?:")
if espresso_shot == "yes":
    order = coffee + " coffee with extra shot of espresso."
else:
    order = coffee + " coffee." 
print(order)
