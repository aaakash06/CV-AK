import cv2
import numpy as np

bgr = np.zeros((300,300,3))

cv2.imshow("black image",bgr)
cv2.waitKey(0)

bgr[:,:,:] = (0,0,255)

cv2.imshow("red image", bgr)
cv2.waitKey(0)


image = cv2.imread("carr.jpeg")
cv2.imshow("car image original ",image)
cv2.waitKey(0)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("car image rgb", rgb)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("car image gray", gray)
cv2.waitKey(0)

