
import numpy as np
import matplotlib.image as gImage
import matplotlib.pyplot as plt

image = gImage.imread('F:\\AVCodec\\medias\\lena_gray.jpg')

transform = np.fft.fft2(image)
transform = np.fft.fftshift(transform)

for i in range(0, 100):
    transform[i] = 0
    transform[:,i] = 0
for i in range(412, 512):
    transform[i] = 0
    transform[:,i] = 0

plt.imshow(np.log(abs(transform)), 'gray')
plt.show()

image = np.fft.ifft2(transform)
plt.imshow(abs(image), 'gray')
plt.show()