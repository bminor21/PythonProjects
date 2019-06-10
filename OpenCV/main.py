import cv2

image = cv2.imread("galaxy.jpg", 1)

newX = int( image.shape[1] / 2 )
newY = int( image.shape[0] / 2 )
resized_image = cv2.resize( image, (newX, newY))

cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
