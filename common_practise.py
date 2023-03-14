import numpy as np
from numpy.linalg import matrix_power
i=np.array[[0,1],[1,1]]
print(np.matmul(matrix_power(i,20),np.array([1,0]))[1])