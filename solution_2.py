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


# >>>>>>>>>>>>>>> Solution method 2 <<<<<<<<<<<<<<<<<<< #

# PRAKASH NIDHI VERMA - IIIT Jabalpur (CSE)

# NOTE: This solution implimented using by my own developed algorithms which is based on mathmetical approch 
# but its consume some time for execution.

#####################

import cv2
import numpy as np

THRESHOLD = 20
def checkBlack(pixel):
	for i in range(len(pixel)):
		if pixel[i]>THRESHOLD:
			return False
	return True

def getTextOverlay(input_image):

	output = np.zeros(input_image.shape, dtype=np.uint8)
	for r in range(input_image.shape[0]):
		for c in range(input_image.shape[1]):
			if (not checkBlack(input_image[r][c])):
				output[r][c] = [255, 255, 255]
	gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

	# threshhold
	ret, bin = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)

	# closing
	kernel = np.ones((4, 4), np.uint8)
	closing = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)
	inv = cv2.bitwise_not(closing)
	return closing

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################

