import numpy as np
import cv2 as cv
import argparse
import imutils


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to Image")

args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original Image", image)

r = 500.0 / image.shape[0]
dim = (int(image.shape[1] * r), 500)

resized = cv.resize(image, dim, interpolation=cv.INTER_LINEAR)

cv.imshow("Resized (Width) INTERLINEAR", resized)
cv.waitKey(0)

resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)

cv.imshow("Resized (Width) INTERAREA", resized)
cv.waitKey(0)

resized = cv.resize(image, dim, interpolation=cv.INTER_NEAREST)

cv.imshow("Resized (Width) INTERNEAREST", resized)
cv.waitKey(0)

resized = cv.resize(image, dim, interpolation=cv.INTER_CUBIC)

cv.imshow("Resized (Width) INTERCUBIC", resized)
cv.waitKey(0)
