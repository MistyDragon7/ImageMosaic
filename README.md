We made a ImageMosaicing program using OpenCV in order to be able to merge images together and create a panorama.
Initially decided to make my own module using SIFT to match points, RANSAC to create a homography matrix, and cv.warpPerspective to warp the images together. However, I was unable to extend it beyond 2 images, and also the image on the left and right had to be specified earlier.

Therefore, a backup program which was very small was made using the stitch() module available with OpenCV(). This program automatically gathers all jpg files present in the same directory and creates a panorama.

Credits:

https://pylessons.com/OpenCV-image-stiching-continue
https://stackoverflow.com/questions/71261337/i-want-to-know-what-does-np-float32-means

https://docs.opencv.org/3.1.0/d1/d46/group__stitching.html#gsc.tab=0 (Helped me to understand how the stitcher pipeline works).
https://www.geeksforgeeks.org/opencv-panorama-stitching/
https://pythonprogramming.net/feature-matching-homography-python-opencv-tutorial/   (Introduced me to feature matching).

And more parts of the OpenCV documentation.

My Mentor : Vayam Jain.

The Program:
The detailed module: (./main_without_using_stitch.py)
The program using stitch: (./main_using_stitch.py)


How to use:
  For the detailed program, for now you have to edit the code and manually input the image paths; but can be eliminated with a simple input() statement.
  The short program on the other hand, simply picks up all the jpg files in the images subdirectory.
