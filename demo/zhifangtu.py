
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage

image = gImage.imread("F:\\AVCodec\\medias\\1.tif")
result = image.copy()
result.astype('float')
min = result.min()
max = result.max()
beta = 255 / (result.max() - result.min())

for i in range(0, result.shape[0]):
    for j in range(0, result.shape[1]):
        result[i, j] = (result[i, j] - min) * beta

plt.subplot(4, 2, 1)
plt.imshow(result, 'gray')

arr = result.flatten()
plt.subplot(4, 2, 2)
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor="green", alpha=0.75)

image = gImage.imread("F:\\AVCodec\\medias\\1.tif")
result = image.copy()
result[0, 0] = 0
result[0, 1] = 255
plt.subplot(4, 2, 3)
plt.imshow(result, 'gray')

arr = image.flatten()
plt.subplot(4, 2, 4)
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor="green", alpha=0.75)

image = gImage.imread("F:\\AVCodec\\medias\\3.tif")
result = image.copy()
result[0, 0] = 0
result[0, 1] = 255
plt.subplot(4, 2, 5)
plt.imshow(result, 'gray')

arr = image.flatten()
plt.subplot(4, 2, 6)
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor="green", alpha=0.75)

image = gImage.imread("F:\\AVCodec\\medias\\4.tif")
result = image.copy()
result[0, 0] = 0
result[0, 1] = 255
plt.subplot(4, 2, 7)
plt.imshow(image, 'gray')

arr = image.flatten()
plt.subplot(4, 2, 8)
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor="green", alpha=0.75)

plt.show()
