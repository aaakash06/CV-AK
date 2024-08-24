import cv2
import numpy as np
img = cv2.imread('inputs/green_rubik.jpg')
img2 = cv2.imread('inputs/img.jpg')

lower_green = np.array([45,110, 20], dtype=np.uint8)
upper_green= np.array([77,255, 255], dtype=np.uint8)

lower_orange = np.array([1,100, 129], dtype=np.uint8)
upper_orange = np.array([12,255, 255], dtype=np.uint8)

frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

mask_green = cv2.inRange(frame_hsv,lower_green,upper_green)
mask_orange = cv2.inRange(frame_hsv2, lower_orange,upper_orange)


# cv2.imshow("mask_green", mask_green); 
# cv2.waitKey(0)
# cv2.imshow("mask_orange", mask_orange); 
# cv2.waitKey(0)
# img3 = cv2.add(mask_green,mask_orange)
# cv2.imshow("mask_net", img3); 
# cv2.waitKey(0)
# 254 254
# img4 = cv2.subtract(img,img2)
# cv2.imshow('img4',img4)
# cv2.waitKey(0)
# 1 5 = -4 => 4

# img5 = cv2.absdiff(img2,img)


# cv2.imshow('img5',img5)
# cv2.waitKey(0)