import numpy as np


def bra(ket):
    
    return np.matrix(np.array([np.conj(ket[0][0]), np.conj(ket[1][0])]))


def partial_trace(rho, qubit):
    
    if qubit == "A":
        
        return np.kron(unity_n2,bra(zero))*rho*np.kron(unity_n2,zero) + np.kron(unity_n2,bra(one))*rho*np.kron(unity_n2,one)
    
    elif qubit == "B":
    
        return np.kron(bra(zero),unity_n2)*rho*np.kron(zero,unity_n2) + np.kron(bra(one),unity_n2)*rho*np.kron(one,unity_n2)
    
    
def mixedness(matrix):
    
    return 1-np.trace(matrix*matrix)
        


plus = (1/np.sqrt(2)) * np.matrix([[1], [1]])
minus = (1/np.sqrt(2)) * np.matrix([[1], [-1]])
zero = np.matrix([[1], [0]])
one = np.matrix([[0], [1]])

plus_rho = plus * bra(plus)
minus_rho = minus * bra(minus)
zero_rho = zero * bra(zero)
one_rho = one * bra(one)

unity_n2 = zero*bra(zero) + one*bra(one)
 

state = (1/4) * np.kron((1/3) * zero_rho + (2/3) * one_rho, plus_rho) + (3/4) * np.kron(zero_rho, (1/2) * plus_rho + (1/2) * minus_rho)


print("original state:")
print(state)
print("with mixedness:")
print(mixedness(state))

print("")

print("subsystem A:")
print(partial_trace(state,"A"))
print("with mixedness:")
print(mixedness(partial_trace(state,"A")))

print("")

print("subsystem B:")
print(partial_trace(state,"B"))
print("with mixedness:")
print(mixedness(partial_trace(state,"B")))




    

