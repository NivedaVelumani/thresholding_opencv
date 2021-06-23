import cv2
img=cv2.imread("old_book.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
cv2.imwrite("GrayImage.png",gray)


gaussian_blur=cv2.GaussianBlur(gray,(5,5),10)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
cv2.imwrite("gaussian_blur.png" , gaussian_blur)


adaptive_thres=cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 5)
cv2.imshow("ADAPTIVE THRESHOLD",adaptive_thres)
cv2.waitKey(0)

cv2.imwrite("adaptive_thres.jpg",adaptive_thres)
