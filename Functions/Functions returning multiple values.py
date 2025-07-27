import math
def circle(radius):
    area=radius**2*math.pi
    circumference=2*radius*math.pi
    return area,circumference
a,c=circle(4)
area=round(a,2)
circum=round(c,2)
print("Area=", area, "Circumference=",circum)
