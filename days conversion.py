days=int(input("enter the no of days: "))
y=int(days/365)
a=days%365
m=int(a/30)
b=a%30
w=int(b/7)
d=b%7
print(y,"years",m,"months",w,"weeks",d,"days")