import numpy as np



psi = np.matrix([[np.sqrt(2)+5j], [3]])

sigma_x = np.matrix([[0,1],[1,0]])
sigma_z = np.matrix([[1,0],[0,-1]])



def bra(ket):
    
    return np.matrix(np.array([np.conj(ket[0][0]), np.conj(ket[1][0])]))


def size(ket):
    
    return np.sqrt(bra(ket)*ket)


def normalize(ket):
    
    return ket*(1/size(ket))


def ortho(ket):
    
    return np.matrix(  [ [np.conj(np.array(ket)[1][0])], [-np.conj(np.array(ket)[0][0])] ]  )


def exp_val(state,operator):
    
    return bra(state)*operator*state



print("Input ket-vector:")
print(psi)
print("")

print("Corresponding bra-vector:")
print(bra(psi))
print("")

print("Size of these vectors:")
print(size(psi))
print("")

print("Normalized ket-vector:")
print(normalize(psi))
print("")

print("One orthogonal vector:")
print(ortho(psi))
print("")

print("Orthogonality test:")
print(bra(ortho(psi))*psi)
print("")

print("Projector test:")
print( normalize(psi)*bra(normalize(psi)) + normalize(ortho(psi))*bra(normalize(ortho(psi))) )
print("")

print("Expectation value of sigma_x:")
print( exp_val(normalize(psi),sigma_x) )
print("")

print("Expectation value of sigma_z:")
print( exp_val(normalize(psi),sigma_z) )
print("")






