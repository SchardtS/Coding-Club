from SortAlgs import *
import matplotlib.pyplot as plt
import plotly.express as px
import timeit
import random
import numpy as np

N = 10000
X = [random.randint(0, N) for _ in range(N)]

naive_time = timeit.timeit("naive_sort(X, X)", globals=globals(), number=1)
merge_time = timeit.timeit("merge_sort(X, X)", globals=globals(), number=1)
count_time = timeit.timeit("count_sort(X, X)", globals=globals(), number=1)

naive_complexity = lambda n: naive_time/10000**2             * n**2
merge_complexity = lambda n: merge_time/10000/np.log2(10000) * n*np.log2(n)
count_complexity = lambda n: count_time/10000                * n

n = np.logspace(1, 10, 10000)
fig = px.line(x=n, y=naive_complexity(n)/3600/24/365.25, labels={"x": "n", "y": "time [years]"}, title="Naive sort")
fig.add_scatter(x=n, y=merge_complexity(n)/3600/24/365.25, name="Merge sort")
fig.add_scatter(x=n, y=count_complexity(n)/3600/24/365.25, name="Count sort")
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(yaxis=dict(exponentformat="power"), xaxis=dict(exponentformat="power"))
fig.show()