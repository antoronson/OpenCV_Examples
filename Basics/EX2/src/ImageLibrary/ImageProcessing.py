import numpy as np
import cv2 as cv


class ImageProcessing:
    def __init__(self, image):
        self.image = image

    def translate(self, x, y):
        M = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv.warpAffine(self.image, M, (self.image.shape[1], self.image.shape[0]))
        return shifted

    def rotate(self, rotationAngle, center=None, rescale=1.0):
        (center, width, height) = self.getCenterofImage(self.image, center)
        M = cv.getRotationMatrix2D(center, rotationAngle, rescale)
        rotated = cv.warpAffine(self.image, M, (width, height))
        return rotated

    def getCenterofImage(self, center):
        (h, w, l) = self.image.shape  # ((Height, Width, Layer)
        if center is None:
            center = (w // 2, h // 2)
        return (center, w, h)

    def resize(self, width=None, height=None, inter=None):
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
        (h, w) = self.image.shape[:2]

        if width is None and height is None:
            return self.image

        if width is None:
            r = height / float(h)
            dimension = (int(w * r), height)

        if height is None:
            r = width / float(w)
            dimension = (width, int(h * r))

        resized = cv.resize(self.image, dimension, interpolation=inter)

        return resized

    def flipImage(self, horizontal=None, vertical=None):
        """
        Flip an image

        """
        if horizontal is None and vertical is None:
            return self.image

        if horizontal is None:
            flipped = cv.flip(self.image, 1)
            return flipped

        if vertical is None:
            flipped = cv.flip(self.image, 0)
            return flipped

        flipped = cv.flip(self.image, -1)
        return flipped
    def getCroppedImage(self, startX, startY,endX, endY):
        return self.image[startX:endX, startY:endY]