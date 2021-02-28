#  File: Grid.py

#  Description: This program takes in an input file of an any dimension square grid,
              # and finds the largest product of 4 adjacent numbers in any direction.

#  Student Name: Brionna Huynh

#  Student UT EID: bph637

#  Partner Name: Patricia Garcia

#  Partner UT EID: pgg378

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: November 2, 2015

#  Date Last Modified: November 3, 2015

def main():
  
  #Open relevant files
  in_file = open('Grid.txt', 'r')
  
  #Read dimensions
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  #Create an empty grid
  grid = []

  #Populate the grid
  for i in range(dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range(dim):
      row[j] = int(row[j])
    grid.append(row)

  #Create a product list
  prod_list = []

  #Read and multiply blocks of four along rows
  for row in grid:
    for i in range(dim - 3):
      prod = 1
      for j in range(i, i + 4):
        prod = prod * row[j]
        prod_list.append(prod)

  #Read and multiply blocks of four along columns
  for j in range(dim):
    for i in range(dim - 3):
      prod = 1
      for k in range(i, i + 4):
        prod = prod * grid[k][j]
        prod_list.append(prod)
      
  #Read and multiply blocks of four along L-R diagonals
  for i in range(dim - 3):
    for j in range(dim - 3):
      prod = 1
      for k in range(4):
        prod = prod * grid[i + k][j + k]
        prod_list.append(prod)
        
  #Read and multiply blocks of four along R-L diagonals
  for i in range(dim - 3):
    for j in range(dim - 3):
      prod = 1
      for k in range(4):
        prod = prod * grid[i - k][j + k]
        prod_list.append(prod)

  #Display output with max product
  print('The greatest product is ' + str(max(prod_list)) + '.')
  
  #Close file
  in_file.close()

main()
