import numpy as np
import cv2 as cv
import argparse
from ImageLibrary import *
from ImageLibrary.ImageProcessing import ImageProcessing

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Image file path")
args = vars(ap.parse_args())
image = cv.imread(args["image"], 0)

cv.imshow("Original Image", image)

zeros  = np.zeros(image.shape[:2], dtype = "uint8")
cv.imshow("Red", cv.merge([zeros, zeros, image]))
cv.imshow("Green", cv.merge([zeros, image, zeros]))
cv.imshow("Blue", cv.merge([image, zeros, zeros]))

merged = cv.merge([image, image, image])
cv.imshow("Merged", merged)
cv.waitKey(0)
