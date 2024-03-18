# Fitting

## Introduction

Machine learning and deep learning is basically nothing more than a really fancy way of fitting a function to some kind of dataset. Instead of doing the fancy stuff, we want to take a look at the very basics of this procedure. Think of a simple set of measurements $\{y_1, ..., y_n\}$ which were taken at different time points $\{t_1, ..., t_n\}$. Ideally, you want to find a function $f$ such that the error between the function values at each time point is close to the respective measurment, i.e. a function that somehow fits the data. We can realize this by trying to minimize the error between the function values and the measurement. A famous one might be the mean square error:
$$\min_{a \in \mathbb{R^m}} \sum_{i=1}^n (f(t_i, a) - y_i)^2 \qquad m \leq n$$
This minimization problem might look weird at first, but we will try to understand it a bit better. The variables $t_i$ are already fixed values from our experimental measurements, so we cannot consider these to be parameters we try to optimize. Instead, we try to optimize the parameters $a = (a_1, ..., a_m)$ which will define our function. The function we minimize is therefore a function
$$F(a) =  \sum_{i=1}^n (f(t_i, a) - y_i)^2.$$

Here is a tiny example. Imagine a dataset which looks almost like a linear function. In this case you would choose a linear function $f$ which looks like this
$$f(t, a_1, a_2) = a_1*t + a_2$$
Again, we don't want to find $t$, but instead the $a_1$ and $a_2$ which will minimize the function
$$F(a) =  \sum_{i=1}^n (a_1*t_i + a_2 - y_i)^2.$$
So when trying to find the gradient of the function, you will have to consider that you dont take the derivative with respect to $t$, but rather with respect to $a_1$ and $a_2$. Also even though the function you want to plot in the end might be one-dimensional, the dimension of the optimization problem will depend on the number of parameters you want to fit.

## Challenge

There are three datasets:

- `fitting_data_1.csv`
- `fitting_data_2.csv`
- `fitting_data_3.csv`

take any of these datasets and try to find a function which fits the respective data. Use either the gradient method or Newton's method to find 