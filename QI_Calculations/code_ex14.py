import numpy as np

sigma_x = np.array([[0,1],[1,0]])
sigma_y = np.array([[0,-1j],[1j,0]])
sigma_z = np.array([[1,0],[0,-1]])
unity = np.array([[1,0],[0,1]])

state = np.array([[1],[0]])

def rotation(x,y,z,a):
    
    length = np.sqrt(x**2 + y**2 + z**2)
    
    x = x/length
    y = y/length
    z = z/length
    
    return np.cos(a/2) * unity - 1j * np.sin(a/2) * (x * sigma_x + y * sigma_y + z * sigma_z)

print(rotation(0,0,1,np.pi/2))

print(rotation(1,0,0,np.pi).dot(state))

#print(np.exp(1j*np.pi/2)*rotation(0,1,0,np.pi/2).dot(rotation(0,0,1,np.pi)))