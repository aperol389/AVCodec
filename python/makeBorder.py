
import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img = cv2.imread('F:\\AVCodec\\medias\\lena_256.jpg')

plt.figure(1)
plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('origin')

replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
plt.subplot(122)
plt.imshow(replicate, 'gray')
plt.title('REPLICATE')

plt.figure(2)
reflect = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
plt.subplot(121)
plt.imshow(reflect, 'gray')
plt.title('reflect')

constant = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=0)
plt.subplot(122)
plt.imshow(constant, 'gray')
plt.title('constant')

plt.show()
