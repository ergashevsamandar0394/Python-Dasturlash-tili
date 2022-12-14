from math import *
x=float(input("0 va 1 oralig'ida son kiriting >>>"))
y=float(input("y="))
z=float(input("z="))
S=5*atan(x)-(1/4)*acos(x)*((x+3*fabs(x-y)+pow(x,2))/(fabs(x-y)*z+pow(x,2)))
print(f"S={S}")