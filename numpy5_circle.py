from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((240,320))

# This code is exactly the same as the the code from our JS and C++ examples

centrex = 250
centrey = 100
size = 50

for i in range(240):
    for j in range(320):
        x_dist = abs(centrey-i)
        y_dist = abs(centrex-j)
        dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)
        if dist < size:
            myImage[i,j] = 1

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.imshow(myImage, interpolation="bilinear", clim=(0,1), cmap="gray")
plt.show()