
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((512, 512))

for i in range(246, 266):
    for j in range(246, 266):
        image[i,j] = 1

plt.imshow(image, 'gray')
plt.show()

transform = np.fft.fft2(image)
transform = np.fft.fftshift(transform)

for i in range(0, 100):
    transform[i] = 0
    transform[:,i] = 0
for i in range(412, 512):
    transform[i] = 0
    transform[:,i] = 0


plt.imshow(abs(transform), 'gray')
plt.show()

image = np.fft.ifft2(transform)
plt.imshow(abs(image), 'gray')
plt.show()

plt.plot(abs(transform)[256,:])
plt.show()
