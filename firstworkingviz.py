#!/usr/bin/env python3

import random
import cv2
import numpy as np
import time

random.seed(time.time())

winx, winy = 512,513
imgcolor = (255,255,255)

listLength = int(input("length of list to generate: "))

nums = list(range(listLength))

random.shuffle(nums)

# create black background object
def genblackbg(x=winx, y=winy):
	return np.zeros((x,y,3))

# set lines 
def makelines(imagetoinsert):
	for n in nums:
		cv2.line(imagetoinsert, (nums.index(n), winy), (nums.index(n), n), imgcolor, 1)
	
# display starting positions (commented out for now)
# startimg = genblackbg()
# makelines(startimg)
# cv2.imshow('startimg', startimg)

for index in range(1, len(nums)):
	while index > 0 and nums[index - 1] > nums[index]:
		nums[index], nums[index - 1] = nums[index - 1], nums[index]
		index -= 1
	loopimg = genblackbg() 
	makelines(loopimg)	
	cv2.imshow('loopimg', loopimg)
	cv2.waitKey(20)
	
cv2.waitKey(0)
cv2.destroyAllWindows()
