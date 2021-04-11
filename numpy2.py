from matplotlib import pyplot as plt
import numpy as np
import math

myImage = np.zeros((10,10))

myImage[5,6]=1
myImage[3,3]=-1
# myImage[17,3]=8

plt.imshow(myImage, clim=(0,1),cmap="gray")
plt.show()