#  File: GuessingGame.py

#  Description: Guesses the number that the user inputs between numbers 1 and 100.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/13/17

#  Date Last Modified: 11/15/17

def main ():
  a=[]
  for n in range (1, 101):
    a.append(n)
  print("Think of a number between 1 and 100 inclusive.")
  print("And I will guess what it is in 7 tries or less.")
  print()
  ready=input("Are you ready? (y/n):")
  while(ready!="y" and ready!="n"):
    ready=input("Are you ready? (y/n):")
  if(ready=="y"):
    tries=0
    low=0
    high=len(a)-1
    while(tries<7):
      middle=(low+high)//2
      print("Guess", tries+1, ": The number you thought was", a[middle])
      guess=int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct:"))
      print()
      tries+=1
      if(guess==1):
        high=middle-1
        if(high==-1):
          high+=1
      elif(guess==-1):
        low=middle+1
      elif(guess==0):
        print("Thank you for playing the Guessing Game.")
        return
      else:
        guess=int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: 1"))
    if(tries==7):
      print("Either you guessed a number out of range or you had an incorrect entry.")
  else:
    print("Bye")
main()
