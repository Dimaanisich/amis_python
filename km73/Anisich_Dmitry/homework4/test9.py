a=int(input("������ 1=")); c=int(input("������� 1="))
b=int(input("������ 2=")); d=int(input("������� 2="))
s1=a+c; s2=b+d
if s1%2==0:
    k=(s2%2==0)
else:
    k=(s2%2!=0)
if k:
    print("Yes")
else:
    print("No")
