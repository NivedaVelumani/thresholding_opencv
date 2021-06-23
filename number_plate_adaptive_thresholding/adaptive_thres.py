import cv2
img=cv2.imread("number_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
cv2.imwrite("gray_image.png",gray)



gaussian_blur=cv2.GaussianBlur(gray,(7,7),20)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
cv2.imwrite("gaussian_blur.png" , gaussian_blur)


adaptive_thres=cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 7)
cv2.imshow("ADAPTIVE THRESHOLD",adaptive_thres)
cv2.waitKey(0)
cv2.imwrite("adaptive_inv_thresholding.jpg",adaptive_thres)
