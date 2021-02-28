#  File: Day.py

#  Description: Prints the day when a year, month and day is inputed.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/24/17

#  Date Last Modified: 9/25/17

def main():

    year=int(input("Enter year: "))
    while(year<1900 or year>2100):
        year=int(input("Enter year: "))
        
    month=int(input("Enter month: "))
    while(month<1 or month>12):
        month=int(input("Enter month: "))
    if month==2:
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):
                    daysinmonth=29
                else:
                    daysinmonth=28
            else:
                daysinmonth=29
        else:
            daysinmonth=28
    else:
        if month<8 and month%2==1:
            daysinmonth=31
        elif month<8 and month%2==0:
            daysinmonth=30
        elif month>7 and month%2==0:
            daysinmonth=31
        elif month>7 and month%2==1:
            daysinmonth=30
            
    day=int(input("Enter day: "))
    while(day<1 or day>daysinmonth):
        day=int(input("Enter day: "))
    
    if(year>=1900 and year<=1999):
        century=19
    elif(year>=2000 and year<=2099):
        century=20
    elif(year==2100):
        century=21
  
  
    a=month-2
    if (a<1):
        a+=12
        year=year-1

    b=day
    c=(year%100)
    d=century

    w=(13*a-1)//5
    x=c//4
    y=d//4
    z=w+x+y+b+c-2*d
    r=z%7
    r=(r+7)%7


    if(r==0):
        dayname="Sunday"
    if(r==1):
        dayname="Monday"
    if(r==2):
        dayname="Tuesday"
    if(r==3):
        dayname="Wednesday"
    if(r==4):
        dayname="Thursday"
    if(r==5):
        dayname="Friday"
    if(r==6):
        dayname="Saturday"
        
    print("The day is", dayname)
main()
















'''
  if(month==1):
        month1=11
    elif(month==2):
        month1=12
    elif(month==3):
        month1=1
    elif(month==4):
        month1=2
    elif(month==5):
        month1=3
    elif(month==6):
        month1=4
    elif(month==7):
        month1=5
    elif(month==8):
        month1=6
    elif(month==9):
        month1=7
    elif(month==10):
        month1=8
    elif(month==11):
        month1=9
    elif(month==12):
        month1=10
'''





