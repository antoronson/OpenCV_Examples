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


def resize(image, width = None, height = None, inter = None):
    """
        Resize image to the required width, height and interpolation parameter. 
        
        Args:
            image: Input image matrix
            width: resize width
            height: resize height
            inter: Open CV Interpolation params. 
        
        Returns:
            Resized image
    """
    dimension = None
    (h,w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = height/float(h)
        dimension = (int(w*r), height)
    
    if height is None:
        r = width/float(w)
        dimension = (width, int(h*r))

    resized = cv.resize(image, dimension, interpolation = inter)

    return resized

def flipImage(image, horizontal = None, vertical = None):
    """
    Flip an image 

    """
    if horizontal is None and vertical is None:
        return image
    
    if horizontal is None:
        flipped = cv.flip(image, 1)
        return flipped
    
    if vertical is None:
        flipped = cv.flip(image, 0)
        return flipped
    
    flipped = cv.flip(image, -1)
    return flipped
