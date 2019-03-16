
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((256, 256))

for i in range(108, 148):
    for j in range(108, 148):
        image[i, j] = 1

plt.subplot(1, 3, 1)
plt.imshow(image, 'gray')

fft_result = np.fft.fft2(image)
fft_result = np.fft.fftshift(fft_result)

plt.subplot(1, 3, 2)
plt.imshow(abs(fft_result), 'gray')


plt.subplot(1, 3, 3)
plt.imshow(np.log(1 + abs(fft_result)), 'gray')

plt.show()
