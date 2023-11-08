import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(f, df, x, xmin, xmax, α  = 0.3, tol = 1e-4, maxiter = 50):

    x_history = [x]
    f_history = [f(x)]
    while np.linalg.norm(df(x)) > tol:
        x = x - α*df(x)
        x_history.append(x)
        f_history.append(f(x))
        if len(x_history) > maxiter:
            print('Warning: maximum number of iterations reached')
            break

    return x, f(x), x_history, f_history

def visualize_gradient_descent_paths(f, df, x_arr, xmin, xmax, α  = 0.3, tol = 1e-4, maxiter = 50):
    # Plot the function
    x1 = np.linspace(xmin[0],xmax[0],100)
    x2 = np.linspace(xmin[1],xmax[1],100)
    X1, X2 = np.meshgrid(x1, x2)

    plt.rc('font', size=18)
    plt.figure(figsize=(9, 7))
    plt.contourf(X1, X2, f([X1, X2]), 50, cmap='jet', alpha = 0.3)
    plt.colorbar()
    plt.contour(X1, X2, f([X1, X2]), 50, colors='black', linewidths=1, alpha=0.3)

    # Plot the trajectories of the algorithm
    for x0 in x_arr:
        x, fmin, x_history, f_history = gradient_descent(f, df, x0, xmin, xmax, α, tol, maxiter)
        for i in range(len(x_history)-1):
            plt.quiver(*x_history[i], *-α*df(x_history[i]), angles='xy', scale_units='xy', scale=1, color='k', alpha = 0.75)
    
    plt.show()
    return

### Check functions on given example

# Define the function and its gradient
f = lambda x: np.cos(x[0]) + x[1]**2
df = lambda x: np.array([-np.sin(x[0]), 2*x[1]])

# Define the intervals for the plot
xmin = np.array([0, -2])
xmax = np.array([2*np.pi, 2])

# Define the starting points
x1_arr = np.random.uniform(xmin[0], xmax[0], 10)
x2_arr = np.random.uniform(xmin[1], xmax[1], 10)
x_arr = np.array([[x1_arr[i], x2_arr[i]] for i in range(len(x1_arr))])

# Test the gradient descent algorithm using one of the starting points
x, fmin, x_history, f_history = gradient_descent(f, df, x_arr[0], xmin, xmax)
print("The value of x that minimizes f is: ", x)
print("The minimum value of f is: ", fmin)

# Visualize the gradient descent paths
visualize_gradient_descent_paths(f, df, x_arr, xmin, xmax)