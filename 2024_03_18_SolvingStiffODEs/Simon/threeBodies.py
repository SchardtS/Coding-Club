from ODEsolver import solveODE
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Model Parameters
x0 = np.array([-0.602885898116520, 0.252709795391000, -0.355389016941814])
y0 = np.array([1.059162128863347-1, 1.058254872224370-1, 1.038323764315145-1])
vx0 = np.array([0.122913546623784, -0.019325586404545, -0.103587960218793])
vy0 = np.array([0.747443868604908, 1.369241993562101, -2.116685862168820])

T = 10
N = 3000
t = np.linspace(0, T, N)
dt = t[1] - t[0]

def f(u, t):
    x = u[:nofBodies]
    y = u[nofBodies:2*nofBodies]
    vx = u[2*nofBodies:3*nofBodies]
    vy = u[3*nofBodies:]

    du = np.zeros(4*nofBodies)
    for i in range(nofBodies):
        
        du[i] = vx[i]
        du[nofBodies + i] = vy[i]

        for j in range(nofBodies):
            if i != j:
                r = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)
                du[2*nofBodies + i] += - (x[i] - x[j])/r**3
                du[3*nofBodies + i] += - (y[i] - y[j])/r**3
    return du

def df(u, t):
    x = u[:nofBodies]
    y = u[nofBodies:2*nofBodies]
    vx = u[2*nofBodies:3*nofBodies]
    vy = u[3*nofBodies:]

    dxdx = np.zeros((nofBodies, nofBodies))
    dxdy = np.zeros((nofBodies, nofBodies))
    dxdvx = np.eye(nofBodies)
    dxdvy = np.zeros((nofBodies, nofBodies))

    dydx = np.zeros((nofBodies, nofBodies))
    dydy = np.zeros((nofBodies, nofBodies))
    dydvx = np.zeros((nofBodies, nofBodies))
    dydvy = np.eye(nofBodies)
    
    dvxdx = np.zeros((nofBodies, nofBodies))
    dvxdy = np.zeros((nofBodies, nofBodies))
    dvxdvx = np.zeros((nofBodies, nofBodies))
    dvxdvy = np.zeros((nofBodies, nofBodies))
    
    dvydx = np.zeros((nofBodies, nofBodies))
    dvydy = np.zeros((nofBodies, nofBodies))
    dvydvx = np.zeros((nofBodies, nofBodies))
    dvydvy = np.zeros((nofBodies, nofBodies))
    

    for i in range(nofBodies):
        for j in range(nofBodies):
            if i != j:
                r = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)

                # Off Diagonal entries
                dvxdx[i, j] = (3*(x[i] - x[j])**2 - r**2)/r**5
                dvxdy[i, j] = - (3*(x[i] - x[j])*(y[i] - y[j]))/r**5

                dvydx[i, j] = - (3*(x[i] - x[j])*(y[i] - y[j]))/r**5
                dvydy[i, j] = (3*(y[i] - y[j])**2 - r**2)/r**5

                # Diagonal entries
                dvxdx[i, i] += - (3*(x[i] - x[j])**2 - r**2)/r**5
                dvxdx[i, i] += (3*(x[i] - x[j])*(y[i] - y[j]))/r**5

                dvydx[i, i] = - (3*(y[i] - y[j])**2 - r**2)/r**5
                dvydy[i, i] = (3*(x[i] - x[j])*(y[i] - y[j]))/r**5

    return np.block([[dxdx, dxdy, dxdvx, dxdvy], [dydx, dydy, dydvx, dydvy], 
                     [dvxdx, dvxdy, dvxdvx, dvxdvy], [dvydx, dvydy, dvydvx, dvydvy]])


T = 10      # Final time
N = 3000    # Number of time steps

# Initial conditions
x0 = np.array([-0.602885898116520, 0.252709795391000, -0.355389016941814])
y0 = np.array([1.059162128863347-1, 1.058254872224370-1, 1.038323764315145-1])
vx0 = np.array([0.122913546623784, -0.019325586404545, -0.103587960218793])
vy0 = np.array([0.747443868604908, 1.369241993562101, -2.116685862168820])
u0 = np.concatenate((x0, y0, vx0, vy0))

nofBodies = len(x0)

# Solve the ODE
#u, t = solveODE(f, u0, T, N, method = 'explicitEuler')
#u, t = solveODE(f, u0, T, N, method = 'implicitEuler', df = df)
u, t = solveODE(f, u0, T, N, method = 'CN', df = df)

# Plot the solution
xlim = np.array([np.min(u[:,:1*nofBodies])-0.2, np.max(u[:,:1*nofBodies])+0.2])
ylim = np.array([np.min(u[:,1*nofBodies:2*nofBodies])-0.2, np.max(u[:,1*nofBodies:2*nofBodies])+0.2])

fig = plt.figure(figsize=(8,8))
def update(i):
    plt.clf()
    plt.plot(u[:i,0], u[:i,nofBodies], color='k', alpha=0.3)
    plt.scatter(u[i,0], u[i,nofBodies], s=100, color='k', zorder=10)

    plt.plot(u[:i,1], u[:i,nofBodies + 1], color='blue', alpha=0.3)
    plt.scatter(u[i,1], u[i,nofBodies + 1], s=100, color='blue', zorder=10)

    plt.plot(u[:i,2], u[:i,nofBodies + 2], color='y', alpha=0.3)
    plt.scatter(u[i,2], u[i,nofBodies + 2], s=100, color='y', zorder=10)

    plt.gca().set_adjustable("box")
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(xlim)
    plt.ylim(ylim)
    return

frames = np.unique(np.linspace(0, N-1, 500, dtype=int))
ani = FuncAnimation(fig, update, frames=frames, interval=-1)
#ani.save('animation.mp4', fps=60)
plt.show()