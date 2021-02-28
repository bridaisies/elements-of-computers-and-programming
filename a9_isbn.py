#  File: ISBN.py

#  Description: Outputs whether the ISBN is valid or invalid.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637   

#  Course Name: CS303E

#  Unique Number: 51345

#  Date Created: 10/29/17

#  Date Last Modified: 10/30/17

           
def main():
    
    in_File=open("isbn.txt","r")
    read=in_File.readlines()
    line=in_File.readline()
    out_File=open("isbnOut.txt","w")
  
    list1=["0","1","2","3","4","5","6","7","8","9","x","X"]
    for x in range (0,len(read)):
        line=read[x].rstrip("\n")
        og=line
        line=list(line)
        sum_1=0
        s1=[]
        sum_2=0
        s2=[]
        count=0
        a=False
        b=False
    
        if (line[-1]in list1):
            b=True
        
        while "-" in line:
            line.remove("-")
        
        for i in range (0,len(line)):
                      
            if (line[i] in list1):
                a=True
                if (line[i]=="X"):
                    line.remove("X")
                    line.insert(i,"10")
                if (line[i]=="x"):
                    line.remove("x")
                    line.insert(i,"10")               
                if ((line[i] in list1) and (i<=len(line)-2)):
                    count+=1

                line[i]=int(line[i])
                sum_1=sum_1+line[i]
                s1.append(sum_1)
                sum_2=sum_2+s1[i]
                s2.append(sum_2)
            
            else:
                s2=[0]
                break
        if ((a)and(b)and(count==9)and(s2[-1]%11==0)):
            print(og,"valid",file=out_File)
        else:
            print(og,"invalid",file=out_File)
                      
    in_File.close
    out_File.close

main()
