# line no 1 "from...." is an error only specific to Visual code so just run the code using COMMAND PROMPT
#from numpy import *
import numpy as py
a = py.array([[1, 2, 3], [4, 5, 6]])
#a2 = a.flatten()
#a3 = a.reshape(2, 3)
#m = py.matrix(a)
m = py.matrix(' 1,2,3,4,7,9,0 ; 4,5,6,8,3,4 ')
print(m)
print(a)
