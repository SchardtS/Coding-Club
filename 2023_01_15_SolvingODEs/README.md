# Solving ordinary differential equations (ODEs)

## Introduction

ODEs are often used to describe the temporal evolution of some quantity, like position/velocity/acceleration of a particle or population sizes of any species. Most ODEs arise in some general form like this
$$\frac{du(t)}{dt} = f(u), \qquad t \in [0,T]$$
which denotes that the rate of change of $u(t)$. Solving an ODE always starts by looking only at discrete time points $t_0, t_1, ..., t_N$ with $t_0 = 0$ and $t_N = T$. If the number of time steps $N$ is large enough, we can approximate the derivative of a function
$$\frac{du(t_k)}{dt} \approx \frac{u(t_{k+1}) - u(t_k)}{t_{k+1} - t_k}.$$
We use this expression in the differential equation, replace the notation $u(t_k)$ with just $u_k$ and define the step size $\Delta t = t_{k+1}-t_k$ to gain a simple iteration
$$u_{k+1} = u_k + \Delta t f(u_k).$$
The first time step $u_0$ is an initial condition which is usually specified beforehand.

## Challenges

Try to solve at least one of these and plot your solution, i.e. $u(t)$.

### Logistic growth equation

Logistic growth is widely used in population dynamics to describe the self limiting growth of a biological population. Solve the following equation
$$ \frac{du}{dt} = u(1-u), \qquad u_0 = 10^{-6}, \, T = 100$$


### SIR Model

The SIR model aims to describe the course of an epidemic by considering the population of susceptible (S), infected (I) and removed (R) individuals and their interactions towards each other.

$$\begin{align*}
\frac{dS}{dt} &= \nu (S + I + R) - \beta \frac{S I}{S + I + R} - \mu S \\
\frac{dI}{dt} &= \beta \frac{SI}{S + I + R} - \gamma I - \mu I \\
\frac{dR}{dt} &= \gamma I - \mu R \\
S_0 &= 1000, \, I_0 = 3,\,  R_0 = 0,\,  \beta = 0.4,\,  \nu = 0,\,  \gamma = 0.04,\,  \mu = 0, T = 200
\end{align*}$$

Although the equation looks a bit more intimidating, the implementation remains straightforward just with three equations instead of one, i.e. you need three iterations in one time steps
$$\begin{align*}
S_{k+1} &= \dots \\
I_{k+1} &= \dots \\
R_{k+1} &= \dots \\
\end{align*}$$