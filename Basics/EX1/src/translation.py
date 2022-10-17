import numpy as np
import argparse
import cv2
from imutils import *


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "TempData/lion.jpg")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("OriginalImage", image)
cv2.waitKey(0)
shifted = translate(image, 0, 100)
cv2.imshow("Shifted down to Right", shifted)
cv2.waitKey(0)
shifted = translate(image, 100, -200)
cv2.imshow("Shifted left and above", shifted)
cv2.waitKey(0)