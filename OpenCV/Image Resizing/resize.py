import cv2
import glob

images = glob.glob("*.jpg")

for img in images:
    img = cv2.readim(img, 0)
    re = cv2.resize(img, (100,100))
    cv2.imwrite("resized_" + img, re)
