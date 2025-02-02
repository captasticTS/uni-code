import matplotlib.pyplot as plt
import numpy as np
import random as rd

iterations = 1000

omega = 1
delta = 0*omega
gamma = (1/6)*omega
delta_t = 0.1/omega
duration = 30/delta_t

sigma_plus = np.array([[0,1],[0,0]])
sigma_minus = np.array([[0,0],[1,0]])
sigma_x = np.array([[0,1],[1,0]])
unity = np.array([[1,0],[0,1]])


h_opt = -(omega/2) * sigma_x - delta * sigma_plus.dot(sigma_minus)

h_eff = h_opt - 1j * (gamma/2) * sigma_plus.dot(sigma_minus)

phi_initial = np.array([[0],[1]])

    

states = []
photons_all = []

for n in range(iterations):
    
    state = []
    photons_traj = []
    for i in range(int(duration)):
        
        if i == 0:
            state.append(phi_initial)
            photons_traj.append(0)
            continue
        
        state.append( (1 * unity - 1j * delta_t * h_eff).dot(state[i-1]))
        
        probability = 1 - np.linalg.norm(state[i])**2
        
        rd_num = rd.uniform(0, 1)
        
        if rd_num <= probability:
            state[i] = sigma_minus.dot(state[i-1]) / np.sqrt(probability/delta_t)
            photons_traj.append(photons_traj[i-1] + 1)
            
        elif rd_num > probability:
            state[i] = state[i] / np.sqrt(1 - probability)
            photons_traj.append(photons_traj[i-1])
            
    states.append(state)
    photons_all.append(photons_traj)
    
  
    
average_prob = []

for i in range(int(duration)):
    
    average = 0
    for n in range(iterations):
        
        average += np.abs(states[n][i][0])**2
        
    average_prob.append(average/iterations)
    
average_prob_exact_steady = (omega**2) / (2 * omega**2 + 4 * delta**2 + gamma**2)

plt.plot(average_prob)
plt.plot([average_prob_exact_steady] * int(duration))
plt.ylabel("Probability of being in |e>")
plt.xlabel(f"Time per delta_t (delta_t = {delta_t})")
plt.show()



#--------------------------------------------------
#                    PLOTS
#--------------------------------------------------



average_photon = []

for i in range(int(duration)):
    
    average = 0
    for n in range(iterations):
        
        average += photons_all[n][i]
        
    average_photon.append(average/iterations)
    
plt.plot(average_photon)
plt.ylabel("Number of photons")
plt.xlabel(f"Time per delta_t (delta_t = {delta_t})")
plt.show()



squared = []

for i in range(int(duration)):
    
    average = 0
    for n in range(iterations):
        
        average += photons_all[n][i]**2
        
    squared.append(average/iterations)


squared_minus_squared = []

for i in range(int(duration)):
    
    squared_minus_squared.append(squared[i] - average_photon[i]**2)
    
plt.plot(squared_minus_squared)
plt.ylabel("Variance of photon number")
plt.xlabel(f"Time per delta_t (delta_t = {delta_t})")
plt.show()



Q_param = []

for i in range(int(duration)):

    if average_photon[i] == 0:
        Q_param.append(0)
    else:
        Q_param.append((squared_minus_squared[i]/average_photon[i]) - 1)
        
Q_param_exact_steady = (2 * omega**2 * (4 * delta**2 - 3 * gamma**2)) / ((4 * delta**2 + gamma**2 + 2 * omega**2)*2) 
        
plt.plot(Q_param)
plt.plot([Q_param_exact_steady] * int(duration))
plt.ylabel("Q parameter")
plt.xlabel(f"Time per delta_t (delta_t = {delta_t})")
plt.show()