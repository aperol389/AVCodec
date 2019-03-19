
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage
import cv2

image = gImage.imread('F:\\AVCodec\\medias\\skeleton_orig.tif')

plt.figure(1)
plt.title('origin')
plt.imshow(image, 'gray')

image_lap = cv2.Laplacian(image, cv2.CV_16S, ksize = 3)
dst = cv2.convertScaleAbs(image_lap)

plt.figure(2)
plt.title('laplacian')
plt.imshow(dst, 'gray')

image.astype('int16')
image_add = image - image_lap 
image_add = cv2.convertScaleAbs(image_add)

plt.figure(3)
plt.title('add')
plt.imshow(image_add, 'gray')

x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
y = cv2.Sobel(image, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

plt.figure(4)
plt.subplot(1, 3, 1)
plt.imshow(absX, 'gray')
plt.subplot(1, 3, 2)
plt.imshow(absY, 'gray')
plt.subplot(1, 3, 3)
plt.imshow(dst, 'gray')

plt.show()