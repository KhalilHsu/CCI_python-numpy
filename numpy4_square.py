from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((240,320))

# This code is exactly the same as the the code from our JS and C++ examples
TWO_PI = 3.14159 * 2
segments = 600
spacing = TWO_PI * 2 / segments
sizex = 45
sizey = 85
centre = 120

for i in range(240):
    for j in range(320):
        if abs(centre-i) < sizex and abs(centre-j) < sizey:
            myImage[i,j]=1

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.show()