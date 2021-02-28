#  File: CalculatePI.py

#  Description: Calculates the value pi by calling random numbers.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/15/17

#  Date Last Modified: 10/17/17


import math
import random

def computePI(numThrows):
    
    inCircle=0
    for i in range(0, numThrows+1):
        xPos=random.uniform(-1.0, 1.0)
        yPos=random.uniform(-1.0, 1.0)
        hypot=math.hypot(xPos, yPos)
        if hypot<1:
            inCircle+=1
        pie=(inCircle/numThrows*4)
    return pie
    
def main():

    print("Computation of PI using Random Numbers")
    print("")
    numThrows=100
    while numThrows!=100000000:
        pie=computePI(numThrows)
        pie=round(pie,6)
        diff=round(pie-math.pi,6)
        if numThrows==100:
            print ('num =%-d '%numThrows,'      Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        elif numThrows==1000:
            print ('num =%-d '%numThrows,'     Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        elif numThrows==10000:
            print ('num =%-d '%numThrows,'    Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        elif numThrows==100000:
            print ('num =%-d '%numThrows,'   Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        elif numThrows==1000000:
            print ('num =%-d '%numThrows,'  Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        elif numThrows==10000000:
            print ('num =%-d '%numThrows,' Calculated PI = %0f'%pie,'   Difference = %+f'%diff)
        numThrows*=10
    print("")
    print("Difference = Calculated PI - math.pi")

main()

