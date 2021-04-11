from matplotlib import pyplot as plt
import numpy as np
import math

# This is actually five times slower
# but it is easier to write if you are operating in high dimensions.

# you could experiment with many more dimensions. Try adding more...
positions=np.array([[20,40],[50,60]])
# using built in np function for normalised distance
distance = np.linalg.norm(positions[0:1] - positions[1:2])
print (distance)