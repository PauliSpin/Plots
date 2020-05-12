
from polynomials import Polynomial
import numpy as np
import matplotlib.pyplot as plt

# https://www.python-course.eu/matplotlib_legends_and_annotations.php

p = Polynomial(2, 3, -4, 6)
p_der = p.derivative()

print(p)
print(p_der)

fig, ax = plt.subplots()
X = np.linspace(-2, 3, 50, endpoint=True)
F = p(X)
F_derivative = p_der(X)
ax.plot(X, F, label="$" + str(p) + "$")
ax.plot(X, F_derivative, label="$" + str(p_der) + "$")

ax.legend(loc='upper left')
plt.show()
