import numpy as np
import cv2 as cv
img1=cv.imread('beibei.jpg',0)
cv.imshow('beibei',img1)
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('gray.jpg',img1)
    cv.destroyAllWindows()
    