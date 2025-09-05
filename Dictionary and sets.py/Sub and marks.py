maths=int(input("Enter marks:"))
chem=int(input("Enter marks:"))
phy=int(input("Enter marks:"))
d={}
d.update({"Maths": maths})
d.update({"Chem": chem})
d.update({"Phy": phy})
print(d)