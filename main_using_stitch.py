import numpy
import cv2				#OpenCV module, our main tool for the task.
import glob				#glob can be used to open paths of multiple files and import them into a list simultaneously, like a mass select.

img_names = glob.glob('./*.jpg')	#Import all jpg images in the folder and adding their names to a list
images = []
for image in img_names:
	img = cv2.imread(image)		#imported the image into a variable
	images.append(img)		#imported image into a list for mass use.
	cv2.imshow("Image", img)	#image displayed for verififcation
	cv2.waitKey(0)			

Mosaic = cv2.Stitcher_create()		#initialised the stitcher module as variable Mosaic.

error, mosaic = Mosaic.stitch(images)	#final image is stored as mosaic.

if not error:

	cv2.imwrite("StitchedOutput.png", mosaic)	#Storing the mosaic into the same folder.
	cv2.imshow("Mosaic", mosaic)	#Showing the final image.
	cv2.waitKey(0)			#Waits for keypress and then kills the window.

else:
	print("Mosaic failed")
