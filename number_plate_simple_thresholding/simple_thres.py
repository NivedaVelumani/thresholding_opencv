import cv2
#convert color image to grayscale image
img=cv2.imread("number_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)

cv2.imwrite("gray_number_plate.jpg" , gray)

#apply gaussian blur into the image
gaussian_blur=cv2.GaussianBlur(gray,(7,7),20)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)

cv2.imwrite("gaussian_number_plate.jpg",gaussian_blur)

#apply simple thresholding
value,simple_thres=cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("SIMPLE THRESHOLD",simple_thres)
cv2.waitKey(0)

cv2.imwrite("simple_number_plate.jpg",simple_thres)
