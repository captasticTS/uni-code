import numpy as np

sigma_x = np.array([[0,1],[1,0]])
sigma_y = np.array([[0,-1j],[1j,0]])
sigma_z = np.array([[1,0],[0,-1]])
oneone = np.array([[0,0],[0,1]])
zerozero = np.array([[1,0],[0,0]])
unity = oneone + zerozero

unitary = np.array([[np.exp(1j*np.pi),0],[0,np.exp(1j*np.pi)]])

sqrt_sigma_x = ((1-1j)/2)*(unity+1j*sigma_x)


def Cct2(unitary):
    
    return np.kron(zerozero,unity) + np.kron(oneone,unitary)


#print(Cct(unitary))

#print((Cct(np.exp(1j*200)*unity)) - (np.kron(zerozero,unity)+np.kron(oneone,np.exp(1j*200)*unity)))

def CCt3(unitary,control,target):
    
    if control == 2 and target == 3:
        
        return np.kron(unity,np.kron(zerozero,unity) + np.kron(oneone,unitary))
    
    elif control == 1 and target == 3:
        
        return np.kron(zerozero,np.kron(unity,unity)) + np.kron(oneone,np.kron(unity,unitary))
    
    elif control == 1 and target == 2:
        
        return np.kron(np.kron(zerozero,unity) + np.kron(oneone,unitary),unity)
    
    
#print(sqrt_sigma_x)

#print(np.dot(sqrt_sigma_x,sqrt_sigma_x))
    
    
tofoli = np.dot(CCt3(sqrt_sigma_x,1,3),np.dot(CCt3(sigma_x,1,2),np.dot(CCt3(sqrt_sigma_x.conj().T,2,3),np.dot(CCt3(sigma_x,1,2),CCt3(sqrt_sigma_x,2,3)))))

print(tofoli)