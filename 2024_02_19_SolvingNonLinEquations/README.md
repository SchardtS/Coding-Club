# Solving nonlinear Equations

## Introduction

On our way to solve any kind of ODE, we have already seen how to solve linear equations. However, most things in life are unfortunately nonlinear, i.e. we also need a reliable method to solve nonlinear equations. Luckily, there is one prominent method which overshadows most of the others, Newton's method. A short outline for this method looks like this:

- You want to solve an equation $f(x) = 0$ for $x$
- Start with an initial value $x_0$
- Follow the iteration $x_{n+1} = x_{n} - f'(x_n)^{-1}f(x_n)$ until $f(x_n)$ is close to $0$

If the function is one dimensional, then the iteration can also be written as $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$. In higher dimensions, e.g. 2D function with two variables, the derivative of a function at any point $x$ is no longer a scalar value but rather a matrix (also called [Jacobi matrix](https://de.wikipedia.org/wiki/Jacobi-Matrix)). This means, that $f'(x_n)^{-1}f(x_n)$ is actually nothing else than the solution $y$ to the linear equation $f'(x_n)y = f(x_n)$. From our previous meeting, we already know how to solve these types of equations ($Ay=b$). In total, each iteration consists of two essential steps:

- Solve linear equation $f'(x_n)y = f(x_n)$
- Calculate next step $x_{n+1} = x_n - f'(x_n)^{-1}f(x_n)$

If this seems too mathematical right now, then please just go ahead to the challenges. A concrete example might make it easier to understand.


## Challenge

Implement Newton's method as a function. It should take at least three input variables, a function `f`, the function derivative `df` and the initial value for the iteration `x0`. Make sure to stop the iteration as soon as you think you have reached the solution $x$ to the equation $f(x)=0$. In some examples, the derivative will be provided in others you might need to find it yourself.

### Polynomials
- Function: $f(x) = x^4 - 10x^2 + 4$ 
- Derivative: $f'(x) = 4x^3 - 20x$

### Exponential functions
- Function: $f(x) = e^{-x^2} + \frac{1}{10}x$
- Derivative: Try it for yourself!

### Complex functions
- Function: $f(z) = z^5 + 1$ with complex numbers $z = x + iy$
- Derivative: Try it for yourself!

### Two dimensions
- Function:
```math
f(x, y) = \begin{pmatrix} e^{-x^2 - y^2} + \frac{1}{2} \\ x^2 \end{pmatrix}
```
- Derivative:
```math
f'(x, y) = \begin{pmatrix} - 2x e^{-x^2-y^2} & - 2y e^{-x^2-y^2} \\ 2x & 0 \end{pmatrix}
```

Three of these examples have more than one solution. Can you find them all?