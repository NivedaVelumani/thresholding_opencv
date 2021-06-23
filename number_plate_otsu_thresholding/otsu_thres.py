import cv2
img=cv2.imread("number_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)

cv2.imwrite("gray_image.png", gray)
gaussian_blur=cv2.GaussianBlur(gray,(7,7),20)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)

value,otsu_thres=cv2.threshold (gaussian_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("The Threshold value = {}".format(value))
cv2.imshow("OTSU THRESHOLD",otsu_thres)
cv2.waitKey(0)
cv2.imwrite("otsu_number_plate_with gaussian.jpg",otsu_thres)
