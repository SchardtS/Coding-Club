# Solving linear/nonlinear Equations

## Introduction

On our path to solving ODEs of every kind, we want to transition from the explicit Euler method
$$u_{k+1} = u_k + \Delta t f(u_k).$$
to the implicit Euler method.
$$u_{k+1} = u_k + \Delta t f(u_{k+1}).$$
As you can see, the right-hand side now also depends on $u_{k+1}$, so it cannot be solved as simple as before. Instead, it requires us to be able to solve either linear or nonlinear equations. In this exercise we will try to shed light on how to solve linear equations numerically, i.e. equations of the Form
$$Ax = b \qquad \text{also written as} \qquad \begin{pmatrix} a_{11} & \cdots & a_{1n} \\
   \vdots & \ddots & \vdots \\
   a_{n1} & \cdots & a_{nn}\end{pmatrix}
   \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} b_1 \\ \vdots \\ b_n \end{pmatrix}$$

$$Ax = b \qquad \text{also written as} \begin{array}{rrrrr}
4z&+&5&=&25
\end{array}$$
where $A$ is a given matrix and $b$ a given vector. The goal is to find the values of $x$.

## Challenges

There are various methods to solve linear equations, most famously the Gauß elimination method you might already have used in school. However, due to the poor complexity of $\mathcal{O}(n^3)$, one sometimes resorts to iterative methods instead, sacrificing accuracy for reduced computation time. In the following is a collection of various methods for solving linear equations:

- [Gauß Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
- [Jacobi Method](https://en.wikipedia.org/wiki/Jacobi_method)
- [Gauß-Seidel Method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
- [Generalized Minimal Residual (GMRES)](https://en.wikipedia.org/wiki/Generalized_minimal_residual_method)
- [Biconjucgate Gradient Stabilized Method (BiCGstab)](https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method)

Pick a method of your choice and try to implement it. Use your code to solve the linear equation $Ax=b$ with the matrix $A$ from `matrix.txt` and right-hand side vector `b` from `vector.txt`. You can check your solution if you compare it to existing solvers, e.g. `np.linalg.solve(A, b)` in Python or `A\b` in Julia.