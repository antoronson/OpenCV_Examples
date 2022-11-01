import numpy as np
import cv2 as cv
import argparse
from imutils import *


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to Image")

args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original Image", image)

resizedImage = resize(image, width=400, inter=cv.INTER_AREA)

cv.imshow("Resized Image", resizedImage)
cv.waitKey(0)

flippedImage = flipImage(image, horizontal=True, vertical=True)
cv.imshow("Flipped Image", flippedImage)
cv.waitKey(0)
