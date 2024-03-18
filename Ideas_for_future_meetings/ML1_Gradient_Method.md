# Gradient Descent Method

## Introduction

Optimization is the study of finding the maximum or minimum of anything you can express as a mathematical function. It forms the basis of various complex processes, such as fitting, machine learning or deep learning. The gradient descent method is one of the most basic tools to solve optimization problems of the form
$$\min_{x \in \mathbb{R}^n} f(x)$$
which translates to wanting to find the value/vector $x^*$ in an $n$-dimensional space which minimizes the function $f$. The values of $f$ are one-dimensional. The gradient $\nabla f$ of such a function $f$ is a vector that consists of the derivative with respect to each variable in separate entries as seen in this example:
```math
f(x, y) = x^2 + 3xy \qquad \Longrightarrow \qquad \nabla f(x,y) := \begin{pmatrix}\frac{\partial f}{\partial x}(x, y)\\ \frac{\partial f}{\partial y}(x, y)\end{pmatrix} = \begin{pmatrix}2x + 3y\\ 3x\end{pmatrix}.
```
f(x, y) = x^2 + 3xy \qquad \Longrightarrow \qquad \nabla f(x,y) := \begin{pmatrix}\frac{\partial f}{\partial x}(x, y)\\ \frac{\partial f}{\partial y}(x, y)\end{pmatrix} = \begin{pmatrix}2x + 3y\\ 3x\end{pmatrix}.
The gradient has one interesting property, at every position, the gradient is a vector which will always point in the direction of the steepest ascent. It follows, of course, that the negative gradient points in the direction of the steepest descent. This is also the main idea of the gradient descent method. We start with an inital guess $x_0$ for our minimum. Then, we iteratively walk along the negative gradients in order to approach the minimum. The iteration looks like this:
$$x_{k+1} = x_k - \alpha_k \nabla f(x_k)$$
The $\alpha_k$ is the step size (in machine/deep learning it is often called learning rate) and is chosen by the user. This might be a fixed value, or could be adaptive depending on the current state of the method. The iteration should be terminated as soon as you are close enough to the solution, e.g. when the gradient is close to $0$.

## Challenges

### 1D Problem

Although the gradient method is rarely used for 1D problems, it is still possible to do so. Implement the gradient method and use it to find the minimum of the following function
$$f(x) = \log(x^2 + 1) - \cos(x)^2$$
look for the solution in the interval $(-10,10)$. Choose an initial value somewhere in this range and try to find the minimum.

### 2D Problem

Implement the gradient descent method and use it to find the minimum of the following function
$$f(x,y) = cos(x) + y^2$$
with $x \in (0, 2\pi)$ and $y \in (-2,2)$. Choose an initial value somewhere in this range and try to find the minimum.