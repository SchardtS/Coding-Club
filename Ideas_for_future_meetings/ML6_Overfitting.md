# Overfitting

## Introduction

By increasing the number of fitting parameters, you might be able to reduce the mean square error (MSE) very close to zero. This means the the fitting function runs through every point of your data. In theory, for a data set with $n \geq 0$ different values $y_1, ..., y_n$ you can always find a polynomial of degree $n-1$ which perfectly fits the data, i.e.
$$f(x, a) = a_{n-1} x^{n-1} + ... + a_1 x^1 + a_0$$
Although this seems like a perfect fit for your data, you might be disappointed when looking at the actual function itself. This phenomenon of your function fitting suspiciously well to your data points is called overfitting.

## Challenge

Check out the data in `fitting_data_4.csv` and try to make a perfect fit for the data points. Visualize your results and make sure to have a look at the function values of $f$ in between the fitting values.