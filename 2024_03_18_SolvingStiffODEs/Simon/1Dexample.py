from ODEsolver import solveODE
import numpy as np
import matplotlib.pyplot as plt

# Define the ODE
def f(u, t):
    return -1000*(u - np.cos(t))

def df(u, t):
    return -1000

T = 10      # Final time
N = 5000    # Number of time steps
u0 = 0.0    # Initial condition

# Solve the ODE
u_ex, t = solveODE(f, u0, T, N, method = 'explicitEuler')
u_im, t = solveODE(f, u0, T, N, method = 'implicitEuler', df = df)
#u_CN, t = solveODE(f, u0, T, N, method = 'CN', df = df)

# Plot the solution
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 14})
plt.plot(t, u_ex, lw=2, label='explicit Euler', alpha = 0.5)
plt.plot(t, u_im, lw=2, label='implicit, Euler')
#plt.plot(t, u_CN, lw=2, label='Crank-Nicolson')
plt.xlabel('t')
plt.ylabel('u')
plt.legend()
plt.show()