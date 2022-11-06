import numpy as np
import cv2 as cv
import argparse
from ImageLibrary import *
from ImageLibrary.ImageProcessing import ImageProcessing




ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Image file path")
args = vars(ap.parse_args())
image = cv.imread(args["image"])
print(image.shape)
cv.imshow("Original Image", image)
ip = ImageProcessing(image)
(B, G, R) = cv.split(image)
eq_B = ip.eqHist(B)
eq_G = ip.eqHist(G)
eq_R = ip.eqHist(R)

mergedBack = cv.merge([eq_B, eq_G, R])
cv.imshow("Normalized", mergedBack)

cv.waitKey(0)


