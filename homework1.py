#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:25:09 2019

@author: jinyi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:30:34 2019

@author: yijin
"""

import numpy as np

# machine limits epsilon
eps = np.finfo(float).eps
sum = 0
# take average of 1000 run
for j in range(1000):

    # randomize two points within x = [-1,1] y = [-1,1]
    line = np.random.uniform(low=-1, high=1+eps, size=(2,2))
    target_line = np.column_stack((np.ones(2),line[:,0],line[:,1]))
    
    # define ax = b and solve the solution x, 
    b = np.ones(2)
    a = target_line[:,1:]
    x = np.linalg.solve(a, b)
    w = np.concatenate(([-1],x))
    
    # randomize 10 points of training points.   
    data_set = np.random.uniform(low=-1, high=1+eps, size=(10,2))
    
    # Retrive corresponding y points according to line.
    y_value = np.interp(data_set[:,0], line[:,0], line[:,1])
    
    y_set = data_set[:,1]>=y_value
    y_set = 2*(y_set)- 1    
    
    #def convertValue(x):
    #    "This funcion convert True/False to 1/-1"
    #    y = 2*x - 1
    #    return y
    # Extend dimension X_0 as 1.
    x_set = np.column_stack((np.ones(10),data_set[:,0],data_set[:,1]))
    w = np.zeros(3)
    
    def optimize(x,y,w):
        "test"
        y_1 = np.sign(np.matmul(x,w))        
#        print(y_1)
        y_2 = 2*(y_1 == y)-1            
        for idx, value in enumerate(y_2):
            if value == -1:
                w = w + x[idx]*y[idx]
                return w
    
    for i in range(100):
        test = (np.sign(np.matmul(x_set,w)) == y_set)
#        print(i,test)
        if np.all(test):
#            print("success",i+1)
#            print(w)
            sum = sum + i + 1
            break
        else:
            w = optimize(x_set,y_set,w)
            continue

print(sum/1000)        
        
                    
                
                

    
    
        
    





