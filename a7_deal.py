# File: Deal.py

# Description: Shows the output of the game "Let's Make a Deal".

# Student Name: Brionna Huynh   

# Student UT EID: bph637

# Course Name: CS 303E

# Unique Number: 51345

# Date Created: 10/19/17

# Date Last Modified: 10/20/17

def main():

    games=int(input("Enter number of times you want to play: "))
    print("")
    print("  Prize      Guess       View    New Guess")

    switchWins=0

    for i in range(1, games+1):
            
        import random
        prize=random.randint(1,3)
        guess=random.randint(1,3)
        view=random.randint(1,3)
        while(view==guess or view==prize):
            view=random.randint(1,3)
        new=random.randint(1,3)
        while(new==guess or new==view):
            new=random.randint(1,3)
        if(new==prize):
            switchWins=+1
        
        print("   ",prize,"        ",guess,"        ",view,"        ",new)

    print("")
    switch=round((switchWins/games), 2)
    print ("Probability of winning if you switch =", switch)
    noswitch=round((1-switch), 2)
    print ("Probability of winning if you do not switch =", noswitch)
           
main()
