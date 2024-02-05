import numpy as np
    
def solveLinEq(A, b, method='Gauss', tol=1e-10, maxiter=1000):
    if method == 'Gauss':
        x = solveLinEqGauss(A, b)
    elif method == 'bicgstab':
        x = solveLinEqBiCGSTAB(A, b, tol=tol, maxiter=maxiter)
    return x

### Gauss elimination method
def solveLinEqGauss(A, b):
    L, U = LU_decomposition(A)
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Forward substitution (solve Ly = b)
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Backward substitution (solve Ux = y)
    x[-1] = y[-1]/U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:]))/U[i, i]

    return x

### LU decomposition (A = L*U, where L is lower triangular and U is upper triangular)
def LU_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)
    #for i in range(n-1):
    #    for j in range(i+1, n):
    #        L[j, i] = U[j, i]/U[i, i]
    #        U[j, i:] -= L[j, i]*U[i, i:]
    for i in range(n-1):
        L[i+1:, i] = U[i+1:, i]/U[i, i]
        U[i+1:, i:] -= np.outer(L[i+1:, i], U[i, i:])
    return L, U

### BiCGSTAB method
def solveLinEqBiCGSTAB(A, b, tol=1e-10, maxiter=1000):

    x0 = np.zeros(b.shape)
    r0 = b - np.dot(A, x0)
    r0_hat = np.copy(r0)
    rho0 = np.dot(r0, r0_hat)
    p = np.copy(r0)

    for k in range(maxiter):
        v = np.dot(A, p)
        alpha = rho0/np.dot(r0_hat, v)
        h = x0 + alpha*p
        s = r0 - alpha*v

        if np.linalg.norm(s) < tol:
            x = h
            break

        t = np.dot(A, s)
        omega = np.dot(t, s)/np.dot(t, t)
        x = h + omega*s
        r = s - omega*t

        if np.linalg.norm(r) < tol:
            break

        rho = np.dot(r, r0_hat)
        beta = rho/rho0*alpha/omega
        p = r + beta*(p - omega*v)

        x0 = x
        r0 = r
        rho0 = rho
    return x