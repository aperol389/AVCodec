
import cv2

img = cv2.imread('F:\\AVCodec\\medias\\lena_rgb.jpg')
b, g, r = cv2.split(img)
img2 = cv2.merge([b, g, r])

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.imshow("origin", img2)

cv2.waitKey()
