
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage

image = gImage.imread('F:\\AVCodec\\medias\\lena_gray.jpg')

plt.subplot(2,4,1)
plt.title('origin image')
plt.imshow(image, 'gray')

fft_transform = np.fft.fft2(image)
fft_transform = np.fft.fftshift(fft_transform)
print(type(fft_transform))
plt.subplot(2,4,2)
plt.title('fft image')
plt.imshow(np.log(abs(fft_transform)), 'gray')

for i in range(0, 100):
    fft_transform[i] = 0
    fft_transform[:,i] = 0
for i in range(412, 512):
    fft_transform[i] = 0
    fft_transform[:,i] = 0
plt.subplot(2,4,3)
plt.title('cut 100 fft image')
plt.imshow(np.log(abs(fft_transform)), 'gray')

image = np.fft.ifft2(fft_transform)
plt.subplot(2,4,4)
plt.title('cut 100 image')
plt.imshow(abs(image), 'gray')


for i in range(0, 200):
    fft_transform[i] = 0
    fft_transform[:,i] = 0
for i in range(312, 512):
    fft_transform[i] = 0
    fft_transform[:,i] = 0
plt.subplot(2,4,5)
plt.title('cut 200 fft image')
plt.imshow(np.log(abs(fft_transform)), 'gray')

image = np.fft.ifft2(fft_transform)
plt.subplot(2,4,6)
plt.title('cut 100 image')
plt.imshow(abs(image), 'gray')

plt.show()
