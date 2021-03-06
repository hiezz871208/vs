import cv2 

img1 = cv2.imread('tokyo.jpg')
print(img1.shape)

roi1 = img1[400:600,300:700]
roi2 = img1[100:300,800:1200]
dst = cv2.addWeighted(roi1,0.7,roi2,0.3,0)
img1[100:300,800:1200] = dst

cv2.namedWindow('pp',cv2.WINDOW_NORMAL)
cv2.imshow('pp',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
