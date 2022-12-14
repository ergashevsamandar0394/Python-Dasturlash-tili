son=int(input("son kiriting >>>"))
s=0
for i in range(1,son):
    if i%2!=0:
        a=pow(i,2)
        s+=a
        print(f"s={s}")
