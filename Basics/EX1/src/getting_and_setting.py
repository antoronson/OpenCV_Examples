from __future__ import print_function
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True, help ="TempData/")

args = vars(ap.parse_args())
image = cv.imread(args["image"])    # Read image to matrix
#print("width : {} pixels".format(image.shape[1]))
#print("height : {} pixels".format(image.shape[0]))
#print("channels: {}".format(image.shape[2]))

cv.imshow("Image", image)   # Show origin image
#cv.waitKey(0)

#cv.imwrite("TempData/NewImage.jpg", image)

(b,g,r) = image[0,0]

print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

image[0,0] = (0,0,255)

(b,g,r) = image[0,0]

print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

corner = image[0:100, 0:100]    # Get corner 0 ~ 100 pixel of the image
cv.imshow ("Corner", corner) # Show the corner pixels

image[0:100, 0:100] = (0, 0, 255) # (b, g, r ) # change the copied space to green

cv.imshow("Updated", image)
cv.waitKey(0)
