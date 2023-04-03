import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./../../03_data/lena.png')

plt.imshow(img)
plt.show()