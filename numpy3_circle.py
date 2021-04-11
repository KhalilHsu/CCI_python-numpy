from matplotlib import pyplot as plt
import numpy as np
import math

# This doesn't look great, but it is useful to do
# so numpy arrays are column major, not row major.
# So you need to do height first
myImage = np.zeros((240,320))

# This code is exactly the same as the the code frmo
TWO_PI = 3.14159 * 2
segments = 600
spacing = TWO_PI / segments
size = 60

for i in range(segments):
    x = math.cos(spacing * i) * size
    y = math.sin(spacing * i) * size
    myImage[math.floor(x) + 150, math.floor(y) + 80] = 1 # notice we need to floor the output to ints

plt.imshow(myImage, interpolation="bilinear", clim=(0,1), cmap="gray")
plt.show()