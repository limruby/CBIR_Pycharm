import imutils
import cv2
import numpy as np


class Main:
    def __init__(self, bins):
        # store the number of bins for the 3D histogram
        self.bins = bins

    def describe(self, image):
        # convert the img to HSV colour space and initialize
        # the features use to quantify the img
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        # grab dimension and compute the center of the img
        (h, w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))

        # divide img into four rectangles/ segments
        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

        # construct an elliptical mask representing center of img
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
        ellipMask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesY, axesY), 0, 0, 360, 255, -1)

        # loop segments
        for (startX, endX, startY, endY) in segments:

            # Construct mask for each corner of img, subtract ellipse center
            corner_mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(corner_mask, (startX, startY), (endX, endY), 255, -1)
            corner_mask = cv2.subtract(corner_mask, ellipMask)

            # extract colour histogram from img, then update feature vector
            hist = self.histogram(image, corner_mask)
            features.extend(hist)

        # extract colour histogram from elliptical region and update feature vector
        hist = self.histogram(image, ellipMask)
        features.extend(hist)

        # return the feature vector
        return features

    def histogram(self, image, mask):
        # extract 3D colour histogram from masked region of img
        # using supplied number of bins per channel
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])

        # normalize the histogram if using openCV 2.4
        if imutils.is_cv2():
            hist = cv2.normalize(hist, hist)
            return hist.flatten()

        # otherwise handle for OpenCV 3+
        else:
            hist = cv2.normalize(hist, hist)
            return hist.flatten()

        # return histogram
        return hist
