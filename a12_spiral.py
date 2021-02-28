#  File: Spiral.py

#  Description: Outputs the neighboring numbers of the user input number in the spiral in 3 lines.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Partner Name: Patricia Garcia

#  Partner UT EID: pgg378

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/18/17

#  Date Last Modified: 11/20/17

def doTheSpiral(dim, prod):
    
	spiral=[[0]*dim for n in range(dim)]
	count=0
	x=dim-1
	y=dim-1
	col, row=[0, x], [0, y]
	total=dim**2
	a=dim-1
        
	for n in range(total):
		if(count==0):
			spiral[y][x]=total-n
			x=x-1
		elif(count==1):
			spiral[y][x]=total-n
			y=y-1
		elif(count==2):
			spiral[y][x]=total-n
			x=x+1
		elif(count==3):
			spiral[y][x]=total-n
			y=y+1

		if(count==0 and x<col[0]):
			x=col[0]
			row[1]-=1
			y=row[1]
			count=1

		elif(count==1 and y<row[0]):
			y=row[0]
			col[0]+=1
			x=col[0]
			count=2

		elif(count==2 and x>col[1]):
			x=col[1]
			row[0]+=1
			y=row[0]
			count=3

		elif(count==3 and y>row[1]):
			y=row[1]
			col[1]-=1
			x=col[1]
			count=0

	for n in range(len(spiral)):
		for m in range(len(spiral[n])):
			if(spiral[n][m]==prod):
				if((0<n<a) and (0<n<a)):
					print(spiral[n+1][m-1], spiral[n+1][m], spiral[n+1][m+1], end="\n")
					print(spiral[n][m-1], spiral[n][m], spiral[n][m+1], end ="\n")
					print(spiral[n-1][m-1], spiral[n-1][m], spiral[n-1][m+1], end ="\n")
				else:
					print("Number on Outer Edge.")


def main():
    
	print("")
	dim=int(input("Enter dimension: "))
	if(dim%2==0):
		 dim=dim+1
	prod=eval(input("Enter number in spiral: "))
	if(prod>dim**2 or prod<1):
		print("Number not in Range.")
		return
	return doTheSpiral(dim, prod)
main()
