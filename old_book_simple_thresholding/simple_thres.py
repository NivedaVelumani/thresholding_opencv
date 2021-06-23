import cv2
img=cv2.imread("old_book.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
cv2.imwrite("gray_image.png",gray)



gaussian_blur=cv2.GaussianBlur(gray,(7,7),20)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
cv2.imwrite("gaussian_blur.png" , gaussian_blur)


value,simple_thres=cv2.threshold(gaussian_blur, 175 , 255, cv2.THRESH_BINARY_INV)
cv2.imshow("SIMPLE THRESHOLD", simple_thres)
cv2.waitKey(0)
cv2.imwrite("simple_INV_thresholding.jpg", simple_thres)
