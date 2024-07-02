import cv2

image = cv2.imread("carr.jpeg")

cv2.imshow("car red", image)

if cv2.waitKey(0) & 0xff == 27: 
  cv2.destroyAllWindows()

