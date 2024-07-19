import cv2

def showimg(img):
  cv2.imshow("image", img)
  cv2.waitKey(0)
  
image = cv2.imread("carr.jpeg",0)

showimg(image)

thresh = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)[1]
showimg(thresh)