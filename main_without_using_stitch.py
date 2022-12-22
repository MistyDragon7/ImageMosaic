import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange


img_ = cv2.imread('images/first.jpg')       #Image on the right.
img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY) #Converting it to grayscale.
img = cv2.imread('images/second.jpg')       #Image on the left
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)    #Keypoints of Image 1.
kp2, des2 = sift.detectAndCompute(img2,None)    #Keypoints of Image 2.


matcher = cv2.BFMatcher()
matches = matcher.knnMatch(des1,des2, k=2)


# Apply ratio test
useful_matches = []
for m in matches:
	if m[0].distance < 0.5*m[1].distance:     #Applying a ratio rule to only have specific matches which have a certain amount of distance between them at maximum.
		useful_matches.append(m)
	matches = np.asarray(useful_matches)


if len(matches[:,0]) >= 4:
	source= np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)    #Creating a list containing coordinates of all good matching points in image 'first.jpg'.
	destination = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)  #Creating a list containing coordinates of all good matching points in image 'second.jpg'.
	H, masked = cv2.findHomography(source, destination, cv2.RANSAC, 5.0)    #Finding the homography matrix.
	#print H
else:
	raise AssertionError("Can’t find enough keypoints.")


destination = cv2.warpPerspective(img_,H,(img.shape[1] + img_.shape[1], img.shape[0]))  #Warping one image so that it can fit on the other.
plt.subplot(122),plt.imshow(destination),plt.title("Warped Image")      #Displaying the image after warping it.
plt.show()
plt.figure()
destination[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite('output.jpg',destination)                   #Storing the final panorama
plt.imshow(destination)           #Displaying the final panorama.
plt.show()

