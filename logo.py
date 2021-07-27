import cv2 as cv

img1 = cv.imread('tokyo.jpg')
img2 = cv.imread('cjcu.png')
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img2gray,0,100,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

dst = cv.add(img1_bg,img2_fg)
img1 [0:rows,0:cols] = dst

cv.imshow('img2gray',img2gray)
cv.imshow('mask',mask)
cv.imshow('mask_inv',mask_inv)
cv.imshow('img1_bg',img1_bg)
cv.imshow('img2_fg',img2_fg)
cv.imshow('res',img1)
cv.imshow
cv.waitKey(0)
cv.destroyAllWindows()