import numpy as np
import matplotlib.pyplot as plt
from functions import *

# Choose random matrix A
A = np.random.uniform(1,100,(100,100))

# Compute the LU decomposition
L, U = LU_decomposition(A)

# Plot the matrices
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(L, cmap='Blues', vmin=0, vmax=1)
plt.title('Lower triangular matrix')
plt.subplot(1,2,2)
plt.imshow(U, cmap='Reds', vmin=0, vmax=1)
plt.title('Upper triangular matrix')
plt.show()