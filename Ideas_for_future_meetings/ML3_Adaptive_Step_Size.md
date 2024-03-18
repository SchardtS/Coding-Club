# Adaptive Step Sizes

## Introduction

In the last challenge we have seen, that it takes a huge amount of iterations to find the minimum of the Rosenbrock function, depending on the step size. This time we will look at one possibility to choose the step sizes adaptively depending on the current state of the method. In each iteration we will check the following condition:
$$f(x_k - \alpha \nabla f(x_k)) > f(x_k) - \gamma \alpha ||\nabla f(x_k)||^2 \qquad\qquad\qquad \text{(Armijo Condition)}$$
The constant $\gamma$ is typically a tiny value, e.g. $0.1$. Is the Armijo condition fulfilled, we need to decrease the step size $\alpha$ until it is fulfilled. This means that in each iteration of the gradient method we need to start another iteration to find a fitting step size. One way this could look like is:

1. Choose initial step size, e.g. $\alpha_0 = 1$
2. While Armijo condition is fulfilled:
    1. Set $\alpha_{n+1} = \frac{1}{2}\alpha_n$
3. Set gradient method step size $\alpha = \alpha_n$


## Challenge

Let's look again at the Rosenbrock function. Compare the performance of the gradient method without adaptive step size to the one using the Armijo rule.
$$f(x, y) = (1-x)^2 + 100(y-x^2)^2$$
The method might converge in less iterations than previously, but is it also faster?