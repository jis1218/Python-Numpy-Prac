'''
Created on 2018. 3. 10.

@author: Insup Jung
'''
import numpy as np
if __name__ == '__main__':
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a+b) #element-wise
    
    c = [1, 2, 3]
    d = [4, 5, 6]
    print(c+d)
    print(3+b) #Broadcast
    
    e = np.array([[1, 2], [1, 2]])
    f = np.array([[3, 4], [3, 4]])
    print(e+f)
    print(e*f)
    pass