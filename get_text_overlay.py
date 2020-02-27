# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


# >>>>>>>>>>>>>>> Solution method 1 <<<<<<<<<<<<<<<<<<< #

# PRAKASH NIDHI VERMA - IIIT Jabalpur (CSE)

# NOTE:  This solution implimented using by OpenCV-python and the execution time is fast.

#####################

import cv2
import numpy as np
import os

def getTextOverlay(img):
	ret,thresh1 = cv2.threshold(img,20,255,cv2.THRESH_BINARY)
	cv2.imwrite('test.jpg', thresh1)
	img=cv2.imread('test.jpg')

	if os.path.exists("test.jpg"):
	  os.remove("test.jpg")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# threshhold for binary image
	ret,bin = cv2.threshold(gray,245,255,cv2.THRESH_BINARY)

	# closing and remove extra dots lines
	kernel = np.ones((10,10),np.uint8)
	output = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)

	# invert black/white
	inv = cv2.bitwise_not(output)
	return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)