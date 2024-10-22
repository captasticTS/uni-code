import numpy as np

sigma_x = np.array([[0,1],[1,0]])
sigma_y = np.array([[0,-1j],[1j,0]])
sigma_z = np.array([[1,0],[0,-1]])
unity = np.array([[1,0],[0,1]])
oneone = np.array([[0,0],[0,1]])
zerozero = np.array([[1,0],[0,0]])
hadamar = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])

#unitary = np.array([[np.exp(1j*np.pi),0],[0,np.exp(1j*np.pi)]])

def Cct(unitary):
    
    return np.kron(zerozero,unity) + np.kron(oneone,unitary)


def rotation(x,y,z,a):
    
    length = np.sqrt(x**2 + y**2 + z**2)
    
    x = x/length
    y = y/length
    z = z/length
    
    return np.cos(a/2) * unity - 1j * np.sin(a/2) * (x * sigma_x + y * sigma_y + z * sigma_z)


A = rotation(0,1,0,np.pi/4)
B = rotation(0,1,0,-np.pi/4).dot(rotation(0,0,1,-np.pi/2))
C = rotation(0,0,1,np.pi/2)

print(hadamar)
print(np.exp(1j*np.pi/2)*rotation(0,1,0,np.pi/2).dot(rotation(0,0,1,np.pi)))
print(np.exp(1j*np.pi/2)*A.dot(sigma_x.dot(B.dot(sigma_x).dot(C))))

print(np.kron(zerozero,unity)+np.kron(oneone,hadamar))

print("---")

hadamar_general = np.kron(zerozero+np.exp(1j*np.pi/2)*oneone,unity).dot(np.kron(unity,A).dot(Cct(sigma_x).dot(np.kron(unity,B).dot(Cct(sigma_x).dot(np.kron(unity,C))))))

print(hadamar_general)

print("---")

print(np.kron(zerozero,unity)+np.kron(oneone,hadamar) - hadamar_general)