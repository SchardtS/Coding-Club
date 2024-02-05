import numpy as np
import matplotlib.pyplot as plt
from functions import *

A = np.loadtxt('2024_02_05_SolvingLinEquations/matrix.txt')
b = np.loadtxt('2024_02_05_SolvingLinEquations/vector.txt')

# Print the condition number of the matrix
print("The condition number of matrix A is:", int(np.linalg.cond(A)))

# Solve the linear equation system
x = solveLinEq(A, b, method="Gauss", maxiter = 2000)

## Compare the solution with the solution from numpy
x_np = np.linalg.solve(A, b)

# Print absolute and relative error
print('Absolute error: ', np.linalg.norm(x - x_np))
print('Relative error: ', np.linalg.norm(x - x_np) / np.linalg.norm(x_np))

# Plot the solution
plt.plot(b, label='initial vector')
plt.plot(x, label='smooth representation of the vector')
plt.plot(x_np, label='numpy solution')
plt.legend()
plt.show()
