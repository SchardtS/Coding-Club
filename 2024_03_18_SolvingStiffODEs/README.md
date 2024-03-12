# Solving Stiff ODEs

## Introduction

Now that we know how to solve linear and nonlinear equations, we are ready to see another side of ordinary differential equations (ODEs). Without an exact definition, a stiff ODE is usually an equation that operates on different time scales for different variables, meaning that one of them changes rapidly compared to the other. These rapid changes can often lead to numerical instabilities, where the numerical solution will either start to oscillate or explode. Luckily, implicit methods can be used to overcome this problem. The idea behind implicit methods is that the right hand side of the differential equation should be considered not at the current time step, but rather at the next one. For a differential equation $\frac{du}{dt} = f(u)$ we compare the explicit and implicit Euler methods:

$$\begin{align*} 
\text{Explicit Euler Method:} \qquad && u_{k+1} &= u_k + \Delta t f(u_k) \\
\text{Implicit Euler Method:} \qquad && u_{k+1} &= u_k + \Delta t f(u_{k+1})
\end{align*}$$

While the explicit method is easily iterated, the implicit one requires us to solve a nonlinear equation $u_{k+1} - u_k + \Delta t f(u_{k+1}) = 0$ for the unknown variable $u_{k+1}$ which we already know how to do!

## Challenges

You don't need to solve all of these equations, just pick one and have fun!

### Rapidly oscillating 1D example

Implement the explicit and implicit Euler methods for the following equation:
$$\frac{du}{dt} = -1000(u - cos(t))$$
Use the initial condition $u_0 = 0$ and try to evaluate this function in the time span from $0$ to $T=10$ and a number of time steps $N=5000$. Compare both numerical solutions!

### Transcriptional Regulation

In a system where two proteins inhibit each others transcriptional regulation, the equations might look like this:

$$\begin{align*} 
\frac{du}{dt} &= r_u \frac{\eta_u u}{1 + \eta_u u + \eta_v v} - \gamma_u u \\
\frac{du}{dt} &= r_v \frac{\eta_v v}{1 + \eta_u u + \eta_v v} - \gamma_v v
\end{align*}$$

Try to implement this using the explicit and the implicit Euler method. Compare both numerical solutions! Use the following parameters and initial conditions:

````python
# Model Parameters
eta_u = 1
eta_v = 1
r_u = 1
r_v = 1000
gamma_u = 1
gamma_v = 500

# Discretization parameters
T = 10      # Simulation time
N = 1000    # Number of time steps

# Initial conditions
u0 = .9
v0 = .1
````




### Three Body Problem

The three body problem is a famous physical example of three celestial bodies orbiting around in some (hopefully stable) configuration, e.g. moon around earth, earth around sun. The force that holds these bodies together is the gravitational force. Ignoring all of the physical parameters, the equations of motion for three bodies each consist of four equations. Two for the x and y components of the positions and two for the velocities. In total there are 12 equations which look like this:

$$\begin{align*} 
\frac{dx_i}{dt} &= v_x \\
\frac{dy_i}{dt} &= v_y \\
\frac{dv_{x,i}}{dt} &= \sum_{j \neq i} \frac{x_j - x_i}{r_{ij}^3} \\
\frac{dv_{y,i}}{dt} &= \sum_{j \neq i} \frac{x_j - x_i}{r_{ij}^3}
\end{align*}$$

with $r_{ij}$ being the euclidean distance between bodies $i$ and $j$, i.e. $r_{ij} = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$. Try to simulate and visualize this system using the same methods you already learned up to a time of $T=10$ in about $3000$ time steps. You can vary the number of time steps if you don't like the result. Also use the following initial conditions for $x$, $y$, $v_x$, $v_y$:

````python
x0 = [-0.602885898116520, 0.252709795391000, -0.355389016941814]
y0 = [1.059162128863347-1, 1.058254872224370-1, 1.038323764315145-1]
vx0 = [0.122913546623784, -0.019325586404545, -0.103587960218793]
vy0 = [0.747443868604908, 1.369241993562101, -2.116685862168820]
````

This system is not considered a stiff ODE, but it allows us to look at another property of numerical methods, their convergence order. Using only a slight modification of the implicit Euler method will already allow you to see the difference, therefore you have to implement the updating step like this:
$$u_{k+1} = u_{k} + \Delta t \frac{f(u_{k+1}) + f(u_k)}{2}$$
If you have implemented the implicit Euler method before, then you should be able to implement this by changing a single line.