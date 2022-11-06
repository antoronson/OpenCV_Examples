import numpy as np
import cv2 as cv

matRectangle = np.zeros((300, 300), dtype="uint8")

cv.rectangle(matRectangle, (25, 25), (100, 100), 255, -1)
cv.imshow("Rectangle", matRectangle)

matCircle = np.zeros((300, 300), dtype="uint8")

cv.circle(matCircle, (150, 150), 150, 255, -1)
cv.imshow("Circle", matCircle)

cv.waitKey(0)


#Bitwise Operation

bitwiseAnd = cv.bitwise_and(matRectangle, matCircle)
cv.imshow("AND", bitwiseAnd)
cv.waitKey(0)

bitwiseOr = cv.bitwise_or(matRectangle, matCircle)
cv.imshow("OR", bitwiseOr)
cv.waitKey(0)

bitwiseXor = cv.bitwise_xor(matRectangle, matCircle)
cv.imshow("XOR", bitwiseXor)
cv.waitKey(0)

bitwiseNot = cv.bitwise_not(matCircle)
cv.imshow("NOT", bitwiseNot)
cv.waitKey(0)