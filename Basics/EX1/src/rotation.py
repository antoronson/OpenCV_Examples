import numpy as np
import cv2 as cv
import argparse
from imutils import *


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "TempData/lion.jpg")
args = vars(ap.parse_args())
image = cv.imread(args["image"])
cv.imshow("OriginalImage", image)
cv.waitKey(0)

rotated = rotate(image, 45, (25, 35), 1.0)
cv.imshow("Rotated by 45 degree", rotated)

cv.waitKey(0)

rotated = rotate(image, 0)
cv.imshow("Rotated by 90 degree", rotated)
cv.waitKey(0)

"""
Note:
    When passing an argument to a function, Python allows to initialize the param upon function call
    and define default params. When param is not included in function call, default param will be used. 
    However, the next param cannot be a default param without init value. example: rotate function. 
"""