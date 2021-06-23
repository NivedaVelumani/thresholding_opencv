import cv2
img=cv2.imread("old_book.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
cv2.imwrite("Gray_image.png",gray)


#gaussian_blur=cv2.GaussianBlur(gray,(7,7),20)
#cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
#cv2.waitKey(0)



value,otsu_thres=cv2.threshold (gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("The Threshold value = {}".format(value))
cv2.imshow("OTSU THRESHOLD",otsu_thres)
cv2.waitKey(0)
cv2.imwrite("old_page_otsu.jpg",otsu_thres)
