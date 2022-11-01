import numpy as np
import cv2 as cv
import argparse
from ImageLibrary import *
from ImageLibrary.ImageProcessing import ImageProcessing

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Image file path")
args = vars(ap.parse_args())
image = cv.imread(args["image"])

cv.imshow("Original Image", image)


ip = ImageProcessing(image)
resized = ip.resize(width = 500, inter = cv.INTER_AREA)
cv.imshow ("Resized image", resized)
#cv.waitKey(0)

#Crop image

#croppedImage = ip.getCroppedImage(150,200, 500, 500)
#cv.imshow("Cropped Image", croppedImage)
#cv.waitKey(0)
ip.testArithematic()
cv.waitKey(0)