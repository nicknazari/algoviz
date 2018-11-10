#!/usr/bin/env python3

import random
import cv2
import numpy as np
import time

random.seed(time.time())

winx, winy = 512, 512
white = (255,255,255)
red = (0, 0, 255)

listLength = int(input('length of list to generate: '))

nums = list(range(listLength))

random.shuffle(nums)

# create black background object
def genblackbg(x = winx, y = winy):
	return np.zeros((x, y, 3))

# set lines 
def makelines(imagetoinsert, data, redline=None):
	for n in data:
		cv2.line(imagetoinsert, (data.index(n), winy), (data.index(n), n), white, 1)
		if n == redline:
			cv2.line(imagetoinsert, (data.index(n), winy), (data.index(n), n), red, 1)

# display starting positions (commented out for now)
# startimg = genblackbg()
# makelines(startimg)
# cv2.imshow('startimg', startimg)

time.sleep(1.5)

# insertion sort
"""
for index in range(1, len(nums)):
	while index > 0 and nums[index - 1] > nums[index]:
		nums[index], nums[index - 1] = nums[index - 1], nums[index]
		index -= 1
	loopimg = genblackbg() 
	makelines(loopimg, nums, index)	
	cv2.imshow('loopimg', loopimg)
	cv2.waitKey(1)
"""
# radix sort

lst = nums

RADIX = 10
maxLength = False
tmp, placement = -1, 1

while not maxLength:
	maxLength = True
	# declare and initialize buckets
	buckets = [list() for _ in range( RADIX )]

	# split lst between lists
	for i in lst:
		tmp = int((i / placement) % RADIX)
		buckets[tmp].append(i)

		if maxLength and tmp > 0:
			maxLength = False

	# empty lists into lst array
	a = 0
	for b in range( RADIX ):
		buck = buckets[b]
		for i in buck:
			lst[a] = i
			a += 1
			
			loopimg = genblackbg()
			makelines(loopimg, nums, i)
			cv2.imshow('loopimg', loopimg)
			cv2.waitKey(1)

	# move to next
	placement *= RADIX

# merge sort
"""
def merge_sort(collection):
	length = len(collection)


	if length > 1:
		midpoint = length // 2
		left_half = merge_sort(collection[:midpoint])
		right_half = merge_sort(collection[midpoint:])
		i = 0
		j = 0
		k = 0

		
		loopimg = genblackbg()
		makelines(loopimg, collection)
		cv2.imshow('loopimg', loopimg)
		cv2.waitKey(1)

		left_length = len(left_half)
		right_length = len(right_half)
		while i < left_length and j < right_length:
			if left_half[i] < right_half[j]:
				collection[k] = left_half[i]
				i += 1
			else:
				collection[k] = right_half[j]
				j += 1
			k += 1
	
		while i < left_length:
			collection[k] = left_half[i]
			i += 1
			k += 1
	
		while j < right_length:
			collection[k] = right_half[j]
			j += 1
			k += 1

	return collection

merge_sort(nums)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
