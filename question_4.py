import numpy as np
from question_3 import mat 
mat1 = mat[1:4, 1:4] #extracts rows 1 to 3 and columns 1 to 3
print(mat)
print(mat1)

r1 = mat1[0,:] #r1 = mat[0] gives 1st row (aka index 0) , and same is r1 = mat[0,:], the : just means all columns
cL = mat1[:,-1] #this gives last column . I tried searching for how to print it without using : in row, for that we would have to take this matrix's
              #transpose, using a.T syntax
print(r1)
print(cL)
dotprd = np.dot(r1,cL)  #another possible syntax for this would have been, dotprd = r1 @ cL
print("dot proudct of 1st row and 1st column : " , dotprd)