import numpy as np
data = np.array([[170,25,30000],[175,26,36000],[165,24,56000],[150,21,20000]])
print(data.shape) #gives the no of rows and columns

#accessing the data in array

print(data[ : ,  : ]) #rows , columns
print(data[0:3 , : ])
print(data[1:2, : ])

print(data[1:3, 0:3])