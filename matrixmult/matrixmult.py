import numpy as np
 
# input two matrices

file = open("matrix.txt", 'r')
file2 = open("matrix1.txt", 'r')
A = []
B = []
numRows = 0
for row in file:
  A.append([int(x) for x in row.split()])
  numRows += 1; 

for row2 in file2:
  B.append([int(x) for x in row2.split()])

res = np.matmul(A,B)
 
 
# print resulted matrix
with open('result.txt', 'w') as f:

    for i in range(0, numRows):      
        f.write(str(res[i])) #prints one row
        f.write("\n")
