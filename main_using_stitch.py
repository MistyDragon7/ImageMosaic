import numpy
import cv2
import glob

img_names = glob.glob('./*.jpg')
images = []
print(img_names[0])
for image in img_names:
	img = cv2.imread(image)
	images.append(img)
	cv2.imshow("Image", img)
	cv2.waitKey(0)

Mosaic = cv2.Stitcher_create()

error, mosaic = Mosaic.stitch(images)

if not error:

	cv2.imwrite("StitchedOutput.png", mosaic)
	cv2.imshow("Mosaic", mosaic)
	cv2.waitKey(0)

else:
	print("Mosaic failed")
