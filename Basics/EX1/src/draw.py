import numpy as np
import cv2 as cv

canvas = np.zeros((300, 300, 3), dtype ="uint8") # Init 300 x 300 x 3 matrix

green = (0, 255, 0) #(b, g, r)

cv.line(canvas, (0,0), (300, 300), green)
cv.imshow("Canvas", canvas)

cv.waitKey(0)

red = (0, 0, 255)

cv.line(canvas, (300, 0), (0, 300), red, 3)
cv.imshow("Canvas", canvas)

cv.waitKey(0)

