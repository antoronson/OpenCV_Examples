import numpy as np
import cv2 as cv

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, rotationAngle, center = None, rescale=1.0):
    (center, width, height) = getCenterofImage(image, center)
    M = cv.getRotationMatrix2D(center, rotationAngle, rescale)
    rotated = cv.warpAffine(image, M, (width, height))
    return rotated



def getCenterofImage(image, center):
    (h,w,l) = image.shape   #((Height, Width, Layer)
    if center is None:
        center = (w//2, h//2)
    return(center, w, h)
