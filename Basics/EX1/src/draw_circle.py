import numpy as np
import cv2 as cv

canvas = np.zeros((300, 300, 3), dtype="uint8")

# Center calculation

(cX, cY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv.circle(canvas, (cX, cY), r, white, 5)

cv.imshow("Canvas", canvas)
cv.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv.circle(canvas, tuple(pt), radius, color, -1)

cv.imshow("Canvas", canvas)
cv.waitKey(0)
