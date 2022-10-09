from __future__ import print_function
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True, help ="TempData/")

args = vars(ap.parse_args())
image = cv.imread(args["image"])
print("width : {} pixels".format(image.shape[1]))
print("height : {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv.imshow("Image", image)
cv.waitKey(0)

cv.imwrite("TempData/NewImage.jpg", image)
