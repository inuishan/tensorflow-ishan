__author__ = 'ishan'
__time__ = '28/11/16'

"""Softmax."""

scores = [[30, 10, 02], [.30, .10, .02]]

import numpy as np


def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	y = np.exp(x)
	# print(y)
	z = np.divide(y, np.sum(y, axis=0))
	# print(z)
	return z


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
