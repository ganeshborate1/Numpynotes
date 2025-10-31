'''aggregation function - np.sum(Arrayname)- add all
                       np.mean(arrname) - average
                       np.min(Arrayname)-smallest value
                       np.max(Arrayname)-maximum value
                       np.std(Arrayname)- standarad deviation
                       np.sar(Arrayname)- variance'''

import numpy as np 

arr = np.array([10,20,30,40,50])
print(np.sum(arr))
print(np.mean(arr)) 
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))

