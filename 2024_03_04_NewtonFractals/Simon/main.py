import numpy as np
import matplotlib.pyplot as plt
from fractal import Fractal

frac = Fractal(5, 500, [-1, 1], [-1, 1])

# Boring plot of fractal
frac.roots_of_unity()
frac.calculate_fractal()
frac.plot()
plt.show()

# Zoom in on the fractal
#frac.zoom(-0.795, 0, frames=500, fps=30)