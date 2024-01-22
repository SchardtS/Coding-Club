import numpy as np
import matplotlib.pyplot as plt
from functions import solveODE

# Parameters
T = 100
N = 1000
t = np.linspace(0,T,N)

# Initial condition
u0 = np.array([1e-3])

# Right-hand side of ODE
rhs = lambda u, t: u*(1 - u)

# Solve ODE
u = solveODE(rhs, t, u0)
u_exact = 1/(1 + ((1 - u[0])/u[0])*np.exp(-(t-t[0])))

# Plot
plt.figure(figsize=(8,6))
plt.rcParams.update({'font.size': 16})
plt.plot(t, u, 'r', lw=2, label='Numerical solution')
plt.plot(t, u_exact, 'k--', lw=2,  label='Exact solution')
plt.legend()
plt.show()