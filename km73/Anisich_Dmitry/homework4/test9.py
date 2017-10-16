a=int(input("Строка 1=")); c=int(input("Колонка 1="))
b=int(input("Строка 2=")); d=int(input("Колонка 2="))
s1=a+c; s2=b+d
if s1%2==0:
    k=(s2%2==0)
else:
    k=(s2%2!=0)
if k:
    print("Yes")
else:
    print("No")
