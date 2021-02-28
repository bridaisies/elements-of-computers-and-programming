#  File: Goldbach.py

#  Description: Uses the Goldbach's Conjecture to output prime sums for even numbers greater than 4 where both limits are even.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/12/17

#  Date Last Modified: 10/13/17

def is_prime(n):

    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():

    lower=int(input("Enter the lower limit: "))
    upper=int(input("Enter the upper limit: "))
    while(upper%2!=0 or lower%2!=0 or upper<=lower or lower<4):
        lower=int(input("Enter the lower limit: "))
        upper=int(input("Enter the upper limit: "))
        
    for n in range(lower, upper+1, 2):
        print(n, end=" ")
        for a in range(2,(n//2+1)):
            if is_prime(a):
                b=n-a
                if is_prime(b):
                    print("=",a,"+",b,end=" ")
        print()      
    
main()
