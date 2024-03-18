# Newton's Method for Optimization

## Introduction

Newton's method might already be known to you as a simple Method to find the roots of a function, i.e. the values $x^*$ which fulfill $F(x^*)=0$. The Newton iteration looks like this:
$$x_{k+1} = x_k - F'(x_k)^{-1}F(x_k)$$
The roots of a function are not necessarily their minima, i.e. optimization and root finding are not directly related. However, a local minimum $x^*$ for a function $f$ will always satisfy the condition $\nabla f(x^*)=0$. This in return allows us to use Newton's method to find the roots of the gradient, which in turn will (hopefully) lead to a local minimum of a function. Therefore we define the function $F := \nabla f$ and use Newton's method as usual. In total this leads to the iteration
$$x_{k+1} = x_k - H_f(x_k)^{-1} \nabla f(x)$$
The matrix $H_f(x_k)$ is called Hessian matrix at point $x_k$ which is basically the second derivative of $f$, e.g.
```math
f(x, y) = x^3 + 3xy \qquad \Longrightarrow \qquad \nabla f(x,y) := \begin{pmatrix}\frac{\partial f}{\partial x}(x, y)\\ \frac{\partial f}{\partial y}(x, y)\end{pmatrix} = \begin{pmatrix}3x^2 + 3y\\ 3x\end{pmatrix} \qquad \Longrightarrow \qquad H_f(x,y) = \begin{pmatrix}\frac{\partial^2 f}{\partial x \partial x}(x,y) & \frac{\partial^2 f}{\partial y \partial x}(x,y)\\ \frac{\partial^2 f}{\partial x \partial y}(x,y) & \frac{\partial^2 f}{\partial y \partial y}(x,y)\end{pmatrix} = \begin{pmatrix}6x & 3\\ 3 & 0\end{pmatrix}.
```
$$f(x, y) = x^3 + 3xy \qquad \Longrightarrow \qquad \nabla f(x,y) := \begin{pmatrix}\frac{\partial f}{\partial x}(x, y)\\ \frac{\partial f}{\partial y}(x, y)\end{pmatrix} = \begin{pmatrix}3x^2 + 3y\\ 3x\end{pmatrix} \qquad \Longrightarrow \qquad H_f(x,y) = \begin{pmatrix}\frac{\partial^2 f}{\partial x \partial x}(x,y) & \frac{\partial^2 f}{\partial y \partial x}(x,y)\\ \frac{\partial^2 f}{\partial x \partial y}(x,y) & \frac{\partial^2 f}{\partial y \partial y}(x,y)\end{pmatrix} = \begin{pmatrix}6x & 3\\ 3 & 0\end{pmatrix}.$$

## Challenge

Take any example from the previous challenges and try to use Newton's method to find the local minimum of the respective function. Compare the performance (number of iterations / runtime) between Newton's method and the gradient method.