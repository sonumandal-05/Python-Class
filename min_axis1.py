import numpy as np
l=[[3,4,6],[7,8,9]]
arr=np.array(l)
print(np.min(arr, axis=1)) # minimum of each row
print(np.min(arr, axis=0)) # minimum of each column