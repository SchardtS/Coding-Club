# Example Coding Challenge

# Some context (not always necessary for your challenges)

Finding the minimum of a mathematical function, fitting a function to some data and even machine learning / deep learning rely on the same simple algorithm, the gradient descent method. The method itself follows a simple idea. If you have a function $f(x)$ and want to find a local minimum, you start with an initial guess $x_0$ and follow the iteration rule
$$x_{n+1} = x_n - \alpha_n \nabla f(x_n).$$
The notation $\nabla f$ denotes the gradient of $f$, which is defined as the vector of the (partial) derivatives of $f$ in each direction. A simple 2D example:
$$f(x, y) = x^2 + 3xy \qquad \Longrightarrow \qquad \nabla f(x,y) := \begin{pmatrix}\frac{\partial f}{\partial x}(x, y)\\ \frac{\partial f}{\partial y}(x, y)\end{pmatrix} = \begin{pmatrix}2x + 3y\\ 3x\end{pmatrix}.$$
The $\alpha_n$ is the step size (in ML it is often called learning rate) and is chosen by the user.

# Actual Challenge

Implement the gradient descent method and use it to find the minimum of the following function
$$f(x,y) = cos(x) + y^2$$
with $x \in (0, 2\pi)$ and $y \in (-2,2)$. Choose an initial value somewhere in this range and try to find the minimum. Let's say an optimum is reached if the norm of the gradient of $f$ at that specific point is nearly zero, e.g. $|\nabla f (x)| < 10^{-4}$.