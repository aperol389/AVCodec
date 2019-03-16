
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage

image = gImage.imread("F:\\AVCodec\\medias\\log2.tif")

plt.subplot(2,2,1)
plt.imshow(image, 'gray')

result = [np.power(x, 0.6) for x in image]
plt.subplot(2,2,2)
plt.imshow(result, 'gray')

result = [np.power(x, 0.4) for x in image]
plt.subplot(2,2,3)
plt.imshow(result, 'gray')

result = [np.power(x, 0.3) for x in image]
plt.subplot(2,2,4)
plt.imshow(result, 'gray')

plt.show()