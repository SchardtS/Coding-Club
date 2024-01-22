import numpy as np
import matplotlib.pyplot as plt

def solveODE(rhs, t, u0, solver='explicit_euler'):
    u = np.empty((len(t), len(u0)))
    u[0] = u0

    if solver == 'explicit_euler':
        for k in range(len(t)-1):
            u[k+1] = u[k] + rhs(u[k], t[k])*(t[k+1] - t[k])

    return u