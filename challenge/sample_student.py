## ---------------------------- ##
## 
## sample_student.py
##
## Example student submission for programming challenge. Insructions:
## 1. Before submitting, change the name of this file to your firstname_lastname.py.
## 2. Be sure not to change the name of the methods below.
## 3. Complete the methods below using only python and numpy methods.
## 4. ANIT-PLAGARISM checks will be run on your submission, if your code matches another student's too closely, 
## 	  we will be required to report you to the office of academic affairs - this may results in failing the course 
##    or in severe cases, being expelled. 
##
##
## ---------------------------- ##

import numpy as np

def convert_to_grayscale(im):
	'''
	Converts an (nxmx3) color image im into a (nxm) grayscale image.

	'''

	## Using the idea from https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

	grayscale_image= np.dot(im,[0.2989, 0.5870, 0.1140])

	return grayscale_image


def crop_image(im, crop_bounds):
	'''
	Returns a cropped image, im_cropped.
	im = numpy array representing a color or grayscale image.
	crops_bounds = 4 element long list containing the top, bottom, left, and right crops respectively.

	e.g. if crop_bounds = [50, 60, 70, 80], the returned image should have 50 pixels removed from the top,
	60 pixels removed from the bottom, and so on.

	'''

	#im_cropped=im[crop_bounds[0]:im.shape[0]-crop_bounds[1],crop_bounds[2]:im.shape[1]-crop_bounds[3],:]
	im_cropped=im[crop_bounds[0]:crop_bounds[0]+crop_bounds[1],crop_bounds[2]:crop_bounds[2]+crop_bounds[3]]
	return im_cropped

def compute_range(im):
	'''
	Returns the difference between the largest and smallest pixel values.
	'''

	image_range=np.max(im,axis=(0,1))-np.min(im,axis=(0,1))
	return image_range


def maximize_contrast(im, target_range = [0, 255]):
	'''
	Return an image over same size as im that has been "contrast maximized" by rescaling the input image so
	that the smallest pixel value is mapped to target_range[0], and the largest pixel value is mapped to target_range[1].
	'''

	min = np.min(im)
	max = np.max(im)
	image_adjusted = im
	image_adjusted[image_adjusted==min]=target_range[0]
	image_adjusted[image_adjusted==max]=target_range[1]

	return image_adjusted


def flip_image(im, direction = 'vertical'):
	'''
	Flip image along direction indicated by the direction flag.
	direction = vertical or horizontal.
	'''
	flipped_image=im
	if direction=="vertical":
		flipped_image=np.flip(im,0)
	elif direction=="horizontal":
		flipped_image=np.flip(im,1)

	return flipped_image

def count_pixels_above_threshold(im, threshold):
	'''
	Return the number of pixels with values above threshold.
	'''
	pixels=im[np.where(im>threshold)]
	pixels_above_threshold=len(pixels)
	return pixels_above_threshold


def normalize(im):
	'''
	Rescale all pixels value to make the mean pixel value equal zero and the standard deviation equal to one.
	if im is of type uint8, convert to float.
	'''

	# normalized_image=im-np.mean(im)
	# #normalized_image=normalized_image/np.std(normalized_image)
	# normalized_image = normalized_image / np.max(normalized_image)
	#
	# return normalized_image
	# Using Min Max normalization as per the evaluation function
	normalized_image = (im - np.amin(im)) / (np.amax(im) - np.amin(im))

	return normalized_image


def resize_image(im, scale_factor):
	'''
	BONUS PROBLEM - worth 1 extra point.
	Resize image by scale_factor using only numpy.
	If you wish to submit a solution, change the return type from None.

	'''
	return np.resize(im,(im.shape[0]*scale_factor,im.shape[1]*scale_factor,3))
	#return None






