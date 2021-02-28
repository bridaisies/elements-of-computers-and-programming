#  File: Hailstone.py

#  Description: Outputs the longest cycle length given a range for the hailstone sequence.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303Es

#  Unique Number: 51345

#  Date Created: 9/27/17

#  Date Last Modified: 9/29/17

def hailstone(n):

    if(n%2==0):
        y=(n//2)
    else:
        y=(3*n+1)
    return y

def main():

    start = int(input("Enter starting number of the range: "))
    print("")
    end = int(input("Enter ending number of the range: "))
    print("")
    
    while start<0 or end<0 or end<start:
        start = int(input("Enter starting number of the range: "))
        end = int(input("Enter ending number of the range: "))
   
    longest_length=0
    num=0
    
    for n in range(start, end+1):
        length=0
        x=n
        while(x>1):
            x=hailstone(x)
            length+=1
        if (x==1) :
            if(length>longest_length):
                longest_length=length
                num=n

    print("The number", num, "has the longest cycle length of", longest_length)

main()


