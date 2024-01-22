
import numpy as np
import matplotlib.pyplot as plt
from functions import solveODE

# Modellparameter
beta = .4         # Infection rate
nu = 0            # Birth rate
gamma = .04       # Recovery/death rate due to infection
mu = 0            # General mortality rate
T = 200           # Time horizon

# Numerische Parameter
N = 1000
t = np.linspace(0,T,N)

# Right-hand side of ODE
def rhs(u, t):
    S,I,R = u
    
    val = np.empty(3)
    val[0] = nu*(S + I + R) - beta*S*I/(S + I + R) - mu*S
    val[1] = beta*S*I/(S + I + R) - gamma*I - mu*I
    val[2] = gamma*I - mu*R
    
    return val

# Initial conditions
S0 = 1000
I0 = 3
R0 = 0
u0 = np.array([S0, I0, R0])

# Solve ODE
u = solveODE(rhs, t, u0)

# Plot
plt.figure(figsize=(8,6))
plt.rcParams.update({'font.size': 16})
plt.plot(t, u[:,0], lw = 2, label='Susceptible')
plt.plot(t, u[:,1], lw = 2, label='Infected')
plt.plot(t, u[:,2], lw = 2, label='Removed')
plt.legend()
plt.show()