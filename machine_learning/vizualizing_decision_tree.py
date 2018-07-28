import numpy as np
import matplotlib.pyplot as plt

dobermann = 1000
shepered = 1000

dober_height = 28 + 4* np.random.randn(dobermann)
shepered_height = 26 + 4* np.random.randn(shepered)

plt.hist([dober_height, shepered_height], stacked=True, color=['r','b'])
plt.show()