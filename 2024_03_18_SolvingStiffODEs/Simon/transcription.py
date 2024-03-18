from ODEsolver import solveODE
import numpy as np
import matplotlib.pyplot as plt

# Model Parameters
eta_u = 1
eta_v = 1
r_u = 1
r_v = 1000
gamma_u = 1
gamma_v = 500


# Define the ODE
def f(y, t):
    u, v = y

    du = r_u*eta_u*u/(1 + eta_u*u + eta_v*v) - gamma_u*u
    dv = r_v*eta_v*v/(1 + eta_u*u + eta_v*v) - gamma_v*v

    return np.array([du, dv])

def df(y, t):
    u, v = y

    dudu = r_u*eta_u*(1 + eta_v*v)/(1 + eta_u*u + eta_v*v)**2 - gamma_u
    dudv = -r_u*eta_u*u*(eta_u + 2*eta_v*v)/(1 + eta_u*u + eta_v*v)**2
    dvdu = -r_v*eta_v*v*(eta_v + 2*eta_u*u)/(1 + eta_u*u + eta_v*v)**2
    dvdv = r_v*eta_v*(1 + eta_u*u)/(1 + eta_u*u + eta_v*v)**2 - gamma_v

    return np.array([[dudu, dudv], [dvdu, dvdv]])

T = 10      # Final time
N = 1000    # Number of time steps
u0 = np.array([.9, .1])    # Initial condition

# Solve the ODE
u_ex, t = solveODE(f, u0, T, N, method = 'explicitEuler')
u_im, t = solveODE(f, u0, T, N, method = 'implicitEuler', df = df)

# Plot the solution
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 14})
plt.plot(t, u_ex[:,0], 'c', lw=2, label='u explicit Euler', alpha = 0.3)
plt.plot(t, u_ex[:,1], 'm', lw=2, label='v explicit Euler', alpha = 0.3)
plt.plot(t, u_im[:,0], 'c', lw=2, label='u implicit Euler')
plt.plot(t, u_im[:,1], 'm', lw=2, label='v implicit Euler')
plt.xlabel('t')
plt.ylabel('u, v')
plt.legend()
plt.show()