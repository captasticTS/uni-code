import numpy as np


#bra transformation
def bra(ket):
    
    return np.matrix(np.array([np.conj(ket[0][0]), np.conj(ket[1][0])]))


#constants
zero = np.matrix([[1], [0]])
one = np.matrix([[0], [1]])
plus = (1/np.sqrt(2)) * (zero + one)
minus = (1/np.sqrt(2)) * (zero - one)

plus_rho = plus * bra(plus)
minus_rho = minus * bra(minus)
zero_rho = zero * bra(zero)
one_rho = one * bra(one)

sigma_x = zero*bra(one) + one*bra(zero)
sigma_z = zero_rho - one_rho

unity_n2 = zero*bra(zero) + one*bra(one)


#gates
hadamard1 = np.kron((sigma_x + sigma_z)/np.sqrt(2),np.kron(unity_n2,np.kron(unity_n2,unity_n2)))
hadamard2 = np.kron(unity_n2,np.kron((sigma_x + sigma_z)/np.sqrt(2),np.kron(unity_n2,unity_n2)))
hadamard3 = np.kron(unity_n2,np.kron(unity_n2,np.kron((sigma_x + sigma_z)/np.sqrt(2),unity_n2)))

c34 = np.kron(unity_n2, np.kron(unity_n2, np.kron(zero_rho, unity_n2))) + np.kron(unity_n2, np.kron(unity_n2, np.kron(one_rho, sigma_x)))
c24 = np.kron(unity_n2, np.kron(zero_rho, np.kron(zero_rho, unity_n2))) + np.kron(unity_n2, np.kron(one_rho, np.kron(unity_n2, sigma_x)))
c14 = np.kron(zero_rho, np.kron(unity_n2, np.kron(unity_n2, unity_n2))) + np.kron(one_rho, np.kron(unity_n2, np.kron(unity_n2, sigma_x)))

rotate = zero_rho + np.exp(1j*np.pi/2)*one_rho

rotate_exc_1 = np.kron(unity_n2, np.kron(rotate, np.kron(rotate, rotate)))
rotate_exc_4 = np.kron(rotate, np.kron(rotate, np.kron(rotate, unity_n2)))


#state definition
state = np.kron(zero,np.kron(zero,np.kron(zero,zero)))


#calculation
state_after = hadamard1 * hadamard2 * hadamard3 * rotate_exc_4 * c34 * c24 * c14 * rotate_exc_1 * hadamard3 * hadamard2 * hadamard1 * state


print("original state:")
print(state)

print("")

print("state after gate operations:")
print(state_after)