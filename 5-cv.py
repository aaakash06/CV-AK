import cv2
def showimg(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)


img = cv2.imread('carr.jpeg')
# showimg(img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)[1]
# showimg(thresh)

cnts,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


for c in cnts:
    a = cv2.contourArea(c)
    if a > 10000:
        print(a)
        cv2.drawContours(img, [c],0,(0,0,255), 3)

showimg(img)