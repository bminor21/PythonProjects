import cv2

video = cv2.VideoCapture(0)

frameCount = 0

while True:
    frameCount += 1
    check, frame = video.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(frameCount)
cv2.destroyAllWindows()
video.release()
