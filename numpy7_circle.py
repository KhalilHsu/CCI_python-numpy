from matplotlib import pyplot as plt
import numpy as np
import math


myImage = np.zeros((240,320))

# uses numpy distance measures but is lots slower..

centre = 100
size = 100

for i in range(240):
    for j in range(320):
        positions=np.array([[i,j],[abs(centre-i),abs(centre-j)]])
        distance = np.linalg.norm(positions[0:1] - positions[1:2])
        if distance < size:
            myImage[i,j] = 1

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.imshow(myImage, interpolation="bilinear", clim=(0,1), cmap="gray")
plt.show()