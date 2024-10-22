import numpy as np


den1 = (1/2)*np.matrix([[1,0],[0,1]])
den2 = (1/2)*np.matrix([[1,1],[1,1]])
den3 = np.matrix([[2,1],[1,-1]])
den4 = (1/2)*np.matrix([[1,(1/2)*(1-(1/2)*1j)],[(1/2)*(1+(1/2)*1j),1]])

den = den4


def trace(matrix):
    
    return np.array(matrix)[0][0]+np.array(matrix)[1][1]


def eigenvalue(matrix):
    
    a = np.array(den)[0][0]
    b = np.array(den)[0][1]
    c = np.array(den)[1][0]
    d = np.array(den)[1][1] 
    
    return ( ((a+d)/2) + np.sqrt( ((a+d)/2)**2 + c*b - a*d) , ((a+d)/2) - np.sqrt( ((a+d)/2)**2 + c*b - a*d) )


def is_denmat(matrix):
    
    return (matrix==matrix.H).all() and trace(matrix)==1 and eigenvalue(matrix)[0]>=0 and eigenvalue(matrix)[1]>=0


def mixedness(matrix):
    
    return 1-trace(matrix*matrix)





#results

print("")
   
print(den)

print("is")

if not is_denmat(den):
    print("not")
    
print("a density matrix.")
      
print("")
      
print("Its mixedness is:")

print(mixedness(den))
