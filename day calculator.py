day=int(input("Enter the day:"))
mnth=int(input("enter the month:"))
year=int(input("enter the year:"))
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0 :
    lp=1
else :
    lp=0
#total year to be calculated
yr=year-1
#converting to leap years
m=int(yr%1600)
d=int(m%400)
b=int(d/100)
n=d%100
#odd days in years
if b==1:
  odd_days_in_years=5
elif b==2:
  odd_days_in_years=3
elif b==3:
  odd_days_in_years=1
else :
  odd_days_in_years=0
#odd days in remaining years
leap_years=int(n/4)
remaining_years=n-leap_years
odd_day=(leap_years*2)+(remaining_years*1)
odd_days_in_week=odd_day%7
#month odd days
if mnth==1:
    uu=day
elif mnth==2:
    uu=3+day
elif mnth==3:
    uu=3+lp+day
elif mnth==4:
    uu=6+lp+day
elif mnth==5:
    uu=8+lp+day
elif mnth==6:
    uu=11+lp+day
elif mnth==7:
    uu=13+lp+day
elif mnth==8:
    uu=16+lp+day
elif mnth==9:
    uu=19+lp+day
elif mnth==10:
    uu=21+lp+day
elif mnth==11:
    uu=24+lp+day
elif mnth==12:
    uu=26+lp+day
else:
    uu=0
odddd=uu%7
lll=odddd+odd_days_in_week+odd_days_in_years
bb=lll%7
if bb==0:
 print("sunday")
elif bb==1:
 print("monday")
elif bb==2:
 print("tuesday")
elif bb==3:
 print("wednesday")
elif bb==4:
 print("thursday")
elif bb==5:
 print("friday")
elif bb==6:
 print("Saturday")
else:
 print("Wrong yr")

