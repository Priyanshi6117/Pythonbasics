maths=int(input("Enter maths marks:"))
chem=int(input("Enter chem marks:"))
phy=int(input("Enter phy marks:"))
d={}
d.update({"Maths": maths})
d.update({"Chem": chem})
d.update({"Phy": phy})
print(d)