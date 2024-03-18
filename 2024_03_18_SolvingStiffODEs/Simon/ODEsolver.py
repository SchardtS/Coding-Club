import numpy as np
    
def solveLinEq(A, b, method='Gauss', tol=1e-10, maxiter=1000):
    if np.isscalar(A) and np.isscalar(b):
        x = b/A
    else:
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

### Newton's method
def Newton(f, df, x0, tol=1e-10, maxiter=100, printsteps=False):
    x = np.copy(x0)
    for k in range(maxiter):
        dx = solveLinEq(df(x), -f(x))
        x = x + dx
        if printsteps:
            print('k =', k, 'x =', x, 'f(x) =', f(x))
        if np.linalg.norm(f(x)) < tol:
            break
    return x

############################################################################################################
############################################################################################################
############################################################################################################

### ODE solver
def solveODE(f, u0, T, N, method = 'explicitEuler', df = None):

    t = np.linspace(0, T, N+1)
    dt = t[1] - t[0]

    ### Choose which method to use
    if method == 'explicitEuler':
        u = explicitEuler(f, u0, t, dt)

    elif method == 'implicitEuler':
        if df is None:
            raise ValueError('derivative must be given for implicit Euler method')
        
        u = implicitEuler(f, df, u0, t, dt)

    elif method == 'CN':  
        if df is None:
            raise ValueError('derivative must be given for implicit Euler method')
        u = CN(f, df, u0, t, dt)

    return u, t

### Explicit Euler method
def explicitEuler(f, u0, t, dt):

    # Check if u0 is a scalar or vector
    if np.isscalar(u0):
        u = np.zeros(len(t))
    else:
        u = np.zeros((len(t), len(u0)))

    u[0] = u0

    # Explicit Euler iteration
    for k in range(len(t)-1):
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u

### Implicit Euler method
def implicitEuler(f, df ,u0, t, dt):

    # Check if u0 is a scalar or vector
    if np.isscalar(u0):
        u = np.zeros(len(t))
        I = 1
    else:
        u = np.zeros((len(t), len(u0)))
        I = np.eye(len(u0))
        
    u[0] = u0

    # Implicit Euler iteration
    for k in range(len(t)-1):
        # Build nonlinear equation and its derivative to solve
        F = lambda x: x - u[k] - dt*f(x, t[k+1])
        dF = lambda x: I - dt*df(x, t[k+1])

        u[k+1] = Newton(F, dF, u[k])

    return u

### Crank-Nicolson method
def CN(f, df, u0, t, dt):

    # Check if u0 is a scalar or vector
    if np.isscalar(u0):
        u = np.zeros(len(t))
        I = 1
    else:
        u = np.zeros((len(t), len(u0)))
        I = np.eye(len(u0))
        
    u[0] = u0

    # Crank-Nicolson iteration
    for k in range(len(t)-1):
        # Build nonlinear equation and its derivative to solve
        F = lambda x: x - u[k] - dt*(f(x, t[k]) + f(u[k], t[k+1]))/2
        dF = lambda x: I - dt*df(x, t[k+1])/2

        u[k+1] = Newton(F, dF, u[k])
    return u