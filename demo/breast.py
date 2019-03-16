
import matplotlib.pyplot as plt
import matplotlib.image as gImage

image = gImage.imread('F:\\AVCodec\\medias\\breast.tif')

plt.subplot(1, 2, 1)
plt.imshow(image, 'gray')

result = [256 - x for x in image]

plt.subplot(1, 2, 2)
plt.imshow(result, 'gray')

plt.show()

