#  File: Benford.py

#  Description: Verifies Benford's Law using the US Census data of 2009.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/28/17

#  Date Last Modified: 11/29/17

def main():

    pop_freq={}

    pop_freq['1']=0
    pop_freq['2']=0
    pop_freq['3']=0
    pop_freq['4']=0
    pop_freq['5']=0
    pop_freq['6']=0
    pop_freq['7']=0
    pop_freq['8']=0
    pop_freq['9']=0

    in_file=open("./Census_2009.txt", 'r')
    header=in_file.readline()
    count=0

    for line in in_file:
        count+=1
        line=line.strip()
        pop_data=line.split()
        pop_num=pop_data[-1]

        if pop_num[0]=='1':
            pop_freq['1']+=1
        elif pop_num[0]=='2':
            pop_freq['2']+=1
        elif pop_num[0]=='3':
            pop_freq['3']+=1
        elif pop_num[0]=='4':
            pop_freq['4']+=1
        elif pop_num[0]=='5':
            pop_freq['5']+=1
        elif pop_num[0]=='6':
            pop_freq['6']+=1
        elif pop_num[0]=='7':
            pop_freq['7']+=1
        elif pop_num[0]=='8':
            pop_freq['8']+=1
        elif pop_num[0]=='9':
            pop_freq['9']+=1

    print ("Digit\tCount\t%")
    for i in range(1,10):
        print ("%d\t%d\t%.1f"%(i, pop_freq[str(i)], 100*(pop_freq[str(i)])/count))

    in_file.close()

main()
