
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage

image = gImage.imread("F:\\AVCodec\\medias\\log3.tif")

plt.subplot(1,4,1)
plt.title("origin")
plt.imshow(image, 'gray')

result = [np.power(x, 3.0) for x in image]
plt.subplot(1,4,2)
plt.title("γ=3.0")
plt.imshow(result, 'gray')

result = [np.power(x, 4.0) for x in image]
plt.subplot(1,4,3)
plt.title("γ=4.0")
plt.imshow(result, 'gray')

result = [np.power(x, 5.0) for x in image]
plt.subplot(1,4,4)
plt.title("γ=5.0")
plt.imshow(result, 'gray')

plt.show()