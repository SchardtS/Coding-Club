# Convergence criteria

## Introduction

A local minimum $x^*$ will always fulfill the condition that the gradient at this point $\nabla f(x^*)$ is zero. Therefore, we mentioned last time that we should terminate the gradient method, when the gradient itself is close to $0$. This time, we will compare different conditions in several cases. All of these conditions have one thing in common, we want them to be less than a specific tolerance $\varepsilon$:

1. Norm of the gradient: $|| \nabla f(x_k) || < \varepsilon$
2. Change in objective function: $|f(x_{k+1}) - f(x_k)| < \varepsilon$
3. Change in variables: $|x_{k+1} - x_k| < \varepsilon$

In many cases each of these conditions might already be enough to ensure that your method converges but it is easy to construct examples where these might not be enough. A simple example would be a function which already has ridiculously low values like $f(x) = 10^{-20}x^2$. In this case, the function itself already admits values so low that it will be difficult to find an ideal tolerance $\varepsilon$. Therefore, it also makes sense to look at changes relative to your initial values:

1. Norm of the gradient: $\frac{|| \nabla f(x_k) ||}{|| \nabla f(x_0) ||} < \varepsilon$
2. Change in objective function: $\frac{|f(x_{k+1}) - f(x_k)|}{|f(x_k)|} < \varepsilon$
3. Change in variables: $\frac{|x_{k+1} - x_k|}{x_k} < \varepsilon$


## Challenge

The Rosenbrock function is a famous example which is often used as a performance check for optimization methods. It looks like this:
$$f(x, y) = (1-x)^2 + 100(y-x^2)^2$$
Try to find its minimum using different convergence criteria and tolerances. Try to combine absolute and relative convergence criteria, with different tolerances (usually, the relative tolerance is chosen to be larger than the absolute one ($\varepsilon_{\text{rel}} > \varepsilon_{\text{abs}}$). Also track the number of iterations you need to get to the solution. SPOILER: The minimum can be found at $(x, y) = (1, 1)$ and the function value at this point is $f(1,1) = 0$.
