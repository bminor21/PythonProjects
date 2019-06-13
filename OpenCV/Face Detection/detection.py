import cv2

fc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("news.jpg")

grey_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

faces = fc.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,255), 3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()