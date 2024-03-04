import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

class Fractal:
    def __init__(self, n, N, xlims, ylims, tol=1e-10, maxiter=500):
        self.N = N
        self.n = n
        self.f = lambda z: z**n - 1
        self.df = lambda z: n*z**(n-1)
        self.xlims = xlims
        self.ylims = ylims
        self.tol = tol
        self.maxiter = maxiter

    def Newton(self, x0):
        x = np.copy(x0)
        mask = np.ones(x0.shape).astype(bool)
        res = np.ones(x0.shape)
        for k in range(self.maxiter):
            dx = - self.f(x[mask])/self.df(x[mask])
            x[mask] = x[mask] + dx

            res[mask] = np.abs(dx)
            mask = res/np.abs(x0) >= self.tol
            x0[mask] = x[mask]

            if np.all(~mask):
                break

        return x
    
    def roots_of_unity(self):
        self.roots = np.array([np.exp(2j*np.pi*k/self.n) for k in range(self.n)])

    def calculate_fractal(self):

        x = np.linspace(self.xlims[0], self.xlims[1], self.N)
        y = np.linspace(self.ylims[0], self.ylims[1], self.N)
        Z = x + 1j*y[:, None]

        convergence = self.Newton(Z)

        self.fractal = np.zeros(Z.shape)
        for k in range(len(self.roots)):
            self.fractal[np.abs(convergence - self.roots[k]) < 1e-6] = k + 1

    def plot(self, cmap='jet'):

        plt.imshow(self.fractal, cmap=cmap, vmin=0, vmax=self.n+1, 
                   extent=(self.xlims[0], self.xlims[1], self.ylims[0], self.ylims[1]))
        
    def find_first_change_from_center(self):
        mid_x = self.N//2
        mid_y = self.N//2

        for i in range(1, mid_x):
            search_array = self.fractal[mid_x-i:mid_x+i, mid_y-i:mid_y+i]
            if np.any(search_array != search_array[i, i]):
                index = np.where(search_array != search_array[i, i])
                self.change_index = (index[0][0] + mid_x - i, index[1][0] + mid_y - i)
                break
        
    def zoom(self, x, y, frames = 10, fps = 60, cmap='jet'):

        fig = plt.figure()
        self.x = x
        self.y = y

        def update(i):
            plt.cla()

            q = 0.97
            xlims = [self.x-1*q**i, self.x+1*q**i]
            ylims = [self.y-1*q**i, self.y+1*q**i]

            frac = Fractal(self.n, self.N, xlims, ylims)
            frac.roots_of_unity()
            frac.calculate_fractal()
            frac.plot(cmap=cmap)

            x = np.linspace(xlims[0], xlims[1], self.N)
            y = np.linspace(ylims[0], ylims[1], self.N)
            Z = x + 1j*y[:, None]
            frac.find_first_change_from_center()
            self.x = Z[frac.change_index[0], frac.change_index[1]].real
            self.y = Z[frac.change_index[0], frac.change_index[1]].imag

            print('Frame:', i, 'of', frames)

            return

        ani = FuncAnimation(fig, update, frames=frames)
        ani.save('2024_03_04_NewtonFractals/Simon/n='+str(self.n)+'_x='+str(x)+'_y='+str(y)+'.mp4', fps=fps, dpi=200, savefig_kwargs={'transparent': True, 'facecolor': 'none'})