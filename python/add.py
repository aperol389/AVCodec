
import numpy as np
import cv2

x = np.uint8([[250, 250], [250, 250]])
print(x)

y = np.uint8([[10, 10], [10, 10]])
print(y)

z = cv2.add(x, y)
print(z)

m = x + y

print(m)

