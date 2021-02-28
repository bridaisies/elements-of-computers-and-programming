#  File: Books.py

#  Description: Outputs the comparison of the words of two authors using two texts from both authors.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 12/4/17

#  Date Last Modified: 12/5/17

word_dict={}
def create_word_dict():
  
  insidewords=open("words.txt", "r")
  for line in insidewords:
    word_dict[line.strip()]=1
    
  insidewords.close()

def parseString(st):
  
  count=""
  for x in range(len(st)):
    
    if(st[x].isalpha() or st[x].isspace()):
      count=count+st[x]
    elif(st[x]=="\'" and st[x+1]!="\'st" ):
      count=count+st[x]
    else:
      count+=" "

  return count

  
def getWordFreq(file):
  
  freq={}
  in_file=open(file, "r")
  
  for line in in_file:
    line=line.rstrip()
    line=line.replace("-", " ")
    if(line.endswith("\'")):
      line=line[:len(line)-1]
    elif(line.endswith("\'s")):
      line=line[:len(line)-2]
      
    for word in (parseString(line)).split():
      if word in freq:
        freq[word]=freq[word]+1
      else:
        freq[word]=1  
  
  in_file.close()
        
  caps=[]
  for key in freq:
    if(key[0].isupper()):
      caps.append(key)
     
  for word in caps:
    
    if(word.lower() in freq):
      freq[word.lower()]+=freq[word]
    elif(word.lower() in word_dict):
      freq[word.lower()]=freq[word]
    del freq[word]
 
  return freq 
  
  
def wordTotal(freq):
  
  sum=0
  for y in freq:
    sum=sum+freq[y]
  return sum  
  

def wordComparison(author1, freq1, author2, freq2):
  
  distinct1=len(freq1)
  total1=wordTotal(freq1)
  
  print(author1)
  print("Total distinct words =", distinct1)
  print("Total words (including duplicates) =", total1)
  print("Ratio (% of total distinct words to total words) =", format(distinct1*100/total1, '.10f'))
  print()
  
  distinct2=len(freq2)
  total2=wordTotal(freq2)
  
  print(author2)
  print("Total distinct words =", distinct2)
  print("Total words (including duplicates) =", total2)
  print("Ratio (% of total distinct words to total words) =", format(distinct2*100/total2, '.10f'))
  print()
  
  diffwords1=0
  samediffwords1=0
  for w in freq1:
    if(not (w in freq2)):
      diffwords1=diffwords1+1
      samediffwords1=samediffwords1+freq1[w]
  print(author1+" used "+str(diffwords1)+" words that "+author2+" did not use.")
  print("Relative frequency of words used by "+author1+" not in common with "+author2+" =", format(samediffwords1*100/total1, '.10f'))
  print()
  
  diffwords2=0
  samediffwords2=0
  for w in freq2:
    if(not (w in freq1)):
      diffwords2=diffwords2+1
      samediffwords2=samediffwords2+freq2[w]
  print(author2+" used "+str(diffwords2)+" words that "+author1+" did not use.")
  print("Relative frequency of words used by "+author2+" not in common with "+author1+" =", format(samediffwords2*100/total2, '.10f'))
  
def main():
  
  create_word_dict()
  
  book1=input("Enter the name of the first book: ")
  book2=input("Enter the name of the second book: ")
  print()
  
  author1=input("Enter the last name of the first author: ")
  author2=input("Enter the last name of the second author: ")
  print()
  
  freq1=getWordFreq(book1)
  freq2=getWordFreq(book2)
  
  wordComparison(author1, freq1, author2, freq2)

main()
