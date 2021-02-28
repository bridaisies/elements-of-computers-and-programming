#  File: DNA.py

#  Description: Outputs the longest common strand sequence between two DNA strands.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/25/17

#  Date Last Modified: 10/26/17

def main():

    print("Longest Common Sequences")
    print("")
    pair1=str(input("Pair 1: "))
    print("")
    pair2=str(input("Pair 2: "))
    print("")
    comm=False
    if(len(pair1)==len(pair2)) or (len(pair1)>len(pair2)):
      lenStr=len(pair2)
      var=lenStr
      maxLen=0
      while(var>0):
        start=0
        while(start+var<=lenStr):
          sub=pair2[start:start+var]
          if(sub in pair1):
                firstChar=pair1.find(sub)
                match=pair1[firstChar:firstChar+len(sub)]
                if(len(match)>=maxLen and len(match)>1):
                    maxLen=len(match)
                    print("Pair 3: "+match)
                    comm=True
          start=start+1
        var-=1
      if(comm!=True):
            print ("Pair 3: No Common Sequence Found")
    elif(len(pair2)>len(pair1)):                   
      lenStr=len(pair1)
      var=lenStr
      maxLen=0
      while(var>0):
        start=0
        while(start+var<=lenStr):
          sub=pair1[start:start+var]
          if(sub in pair2):
                firstChar=pair2.find(sub)
                match=pair2[firstChar:firstChar+len(sub)]
                if(len(match)>=maxLen and len(match)>1):
                      maxLen=len(match)
                      print("Pair 3: "+match)
                      comm=True
          start=start+1
        var-=1
      if(comm!=True):
            print ("Pair 3: No Common Sequence Found")
        
main()
    
