import cv2

img1 = cv2.imread('tokyo.jpg')

print(img1.shape)
print(img1[100,200])
print(img1.item(100,200,1))

roi = img1[400:600,300:700]  
roi[:,:,1]=255

h,w,a =roi.shape
img1[100:300,800:1200] = roi
print(len(roi),len(roi[0]))
img1[10:10+h,10:10+w] = roi
print(img1.size)

cv2.namedWindow('pp',cv2.WINDOW_NORMAL)
cv2.imshow('pp',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)