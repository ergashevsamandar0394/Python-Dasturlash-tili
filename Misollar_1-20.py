########## 1-misol ##########
a=int (input("Kvadrat tomoni uzunligi a="))
P=4*a   # P-perametr
print(f"Kvadrat perametri P={P} ga teng.")
########## 2-misol ##########
a=int (input("Kvadrat tomoni uzunligi a="))
S=a**2  # S-Yuza
print(f"Kvadrat yuzi S={S} ga teng.")
########## 3-misol ##########
a=int (input("a="))  # a-To'g'ri to'rtburchakning eni
b=int (input("b="))  # b-To'g'ri to'rtburchakning bo'yi
P=2*(a+b)
S=a*b
print(f"To'g'ri to'rtburchakning yuzi S={S} ga teng.")
print(f"To'g'ri to'rtburchakning peremetri P={P} ga teng.")
########## 4-misol ##########
d=int (input("d=")) # d- Aylana diametri
pi=3.14    # pi-float tipiga oid o'zgarmas son
L=pi*d     # L-aylana uzunligi
print(f"Aylaning uzunligi L={L} ga teng.")
########## 5-misol ##########
a=int (input("a="))
V=a**3    # V-hajm
S=6*a**2   # S-yuza(to'la sirti)
print(f"Kubni hajmi V={V} va to'la sirti S={S} ga teng.")
########## 6-misol ##########
a=int (input("a="))    # a-asosini eni
b=int (input("b="))    # b-asosini bo'yi
c=int (input("c="))    # c-balandligi
V=a*b*c                # V-hajmmi
S=2*(a*b+b*c+a*c)            # S-yuza(to'la sirti)
print(f"Paraleloped hajmi V={V} va to'la sirti S={S} ga teng.")
########## 7-misol ##########
R=int (input("R="))    # R-doiraning radiusi
pi=3.14
L=2*pi*R
S=pi*R**2
print(f"Doiraning uzunligi L={L} va yuzasi S={S} ga teng.")
########## 8-misol ##########
a=int (input("a="))
b=int (input("b="))
orta_arifmetigi=(a+b)/2
print(f"o'rta_arifmetigi={orta_arifmetigi}")
########## 9-misol ##########
a=int (input("a="))   # a-nomanfiy
b=int (input("b="))   # b-nomanfiy
orta_geometrigi=(a*b)**0.5
print(f"o'rta_geometrigi={orta_geometrigi}")
########## 10-misol ##########
a=int (input("a="))   # a-no'lga teng emas
b=int (input("b="))   # b-no'lga teng emas
yigindi=a+b
kopaytma=a*b
kvatrat_a=a**2
kvatrat_b=b**2
print(f"ikkita sonni yig'indisi={yigindi} \nko'paytmasi={kopaytma} \n1-sonni kvatrati={kvatrat_a} \n2-sonni kvadrati={kvatrat_b}")
########## 11-misol ##########
a=int (input("a="))   # a-no'lga teng emas
b=int (input("b="))   # b-no'lga teng emas
yigindi=a+b
kopaytma=a*b
modul_1=abs(a)        # abs()-modul
modul_2=abs(b)
print(f"ikkita sonni yig'indisi={yigindi} \nko'paytmasi={kopaytma} \n1-sonni moduli={modul_1} \n2-sonni moduli={modul_2}")
########## 12-misol ##########
from math import sqrt,pow,fabs
a=int (input("1-kateti a="))
b=int (input("2-kateti b="))
c=sqrt(a**2+b**2)    # c-gepatenuza
P=a+b+c
print(f"To'g'ri burchakli uchburchakning gepatenuzasi c={c} va peremetri P={P} ga teng.")
########## 13-misol ##########
R1=int (input("1-Aylana radiusi R1="))
R2=int (input("2-Aylana radiusi R2="))
pi=3.14
S1=pi*R1**2
S2=pi*R2**2
S3=pi*(R1-R2)**2
print(f"Aylana yuzi S1={S1} \nS2={S2} \nS3={S3}")
########## 14-misol ##########
L=int (input("Aylana uzunligi L="))
pi=3.14
R=L/(2*pi)
S=pi*R**2
print(f"Aylana radiusi R={R} va yuzi S={S} ga teng.")
########## 15-misol ##########
from math import sqrt,pow,fabs
S=int (input("Aylana Yuzi S="))
pi=3.14
R=sqrt(S/pi)
d=2*R
print(f"Aylana radiusi R={R} va diametri d={d} ga teng.")
########## 16-misol ##########
from math import sqrt,pow,fabs
x1=int (input("x1="))
x2=int (input("x2="))
masofa=fabs(x2-x1)
print(f"ikki nuqta orasidagi masofa {masofa} ga teng.")
########## 17-misol ##########
A=int (input("A="))
B=int (input("B="))
C=int (input("C="))
AC=C-A
BC=C-B
yigindi=AC+BC
print(f"Yig'indi AC+BC={yigindi}")
########## 18-misol ##########
A=int (input("A="))
B=int (input("B="))
C=int (input("C="))
AC=C-A     # A<C<B
BC=B-C
kopaytma=AC*BC
print(f"Ko'paytma AC*BC={kopaytma}")
########## 19-misol ##########
from math import sqrt,pow,fabs
x1=int (input("x1="))        # x1=x2
y1=int (input("y1="))        # y2=y3
x3=int (input("x3="))        # x3=x4
y3=int (input("y3="))        # y1=y4
x2=x1
y2=y3
x4=x3
y4=y1
a=sqrt(pow((x2-x1),2)+pow((y2-y1),2))
b=sqrt(pow((x4-x1),2)+pow((y4-y1),2))
P=2*(a+b)
S=a*b
print(f"perametri P={P} \nYuzasi S={S}")
########## 20-misol ##########
from math import sqrt,pow,fabs
x1=int (input("x1="))
y1=int (input("y1="))
x2=int (input("x2="))
y2=int (input("y2="))
print(f"Ikki nuqta orasidagi masofa {sqrt(pow((x2-x1),2)+pow((y2-y1),2))}")


